import torch
import torch.nn as nn
import torch.nn.init as init
import torch.nn.functional as F
import math
from .MyAE import AE as VAE
from .layers import MPL_Net
import numpy as np


class GlobalEmbing(nn.Module):
    def __init__(self, squence_length, input_dim, emb_dim, z_dim):
        super(GlobalEmbing, self).__init__()
        self.squence_length = squence_length
        self.input_dim = input_dim
        self.emb_dim = emb_dim
        self.z_dim = z_dim

        self.n_steps = 100
        self.label_class = 2

        # وزن زمانی/سکانسی
        self.squence_weight = torch.nn.Parameter(torch.Tensor(self.squence_length), requires_grad=True)

        self.dropout = 0.0
        self.dens_hiddensize1 = 128
        self.dens_hiddensize2 = 64

        self._set_layers()
        self._reset_params()

    def _reset_params(self):
        for p in self.parameters():
            if p.requires_grad:
                if p.dim() > 1:
                    init.kaiming_uniform_(p)
                else:
                    stdv = 1.0 / math.sqrt(p.shape[0])
                    init.uniform_(p, a=-stdv, b=stdv)

    def padding_z(self, z, global_x):
        out_z = []
        for i in range(global_x.shape[0]):
            temp_z = z[:global_x[i]]
            out_z.append(torch.cat(
                [temp_z,
                 torch.zeros(self.n_steps - temp_z.shape[0], self.z_dim,
                             dtype=torch.float32, requires_grad=False, device=z.device)],
                dim=0))
        out_z = torch.stack(out_z)
        return out_z

    def _set_layers(self):
        self.vae = VAE(h_dim=self.emb_dim, input_dim=self.input_dim, z_dim=self.z_dim)
        self.mlp = MPL_Net(
            dens_inputsize=self.z_dim,
            dens_outputsize=self.label_class,
            dens_dropout=self.dropout,
            dens_hiddensize1=self.dens_hiddensize1,
            dens_hiddensize2=self.dens_hiddensize2
        )
        # CrossEntropyLoss: logits خام باید وارد شود (بدون softmax)
        self.criterion = nn.CrossEntropyLoss(
            weight=torch.from_numpy(np.array([0.5 / 0.7, 0.5 / 0.3], dtype=np.float32)),
            reduction='mean'
        )

    def forward(self, batch_global_x, batch_label):

        total_classfier_loss = []
        total_vae_loss = []
        total_classfier_acc = []
        batch_z = []

        for i in range(len(batch_global_x)):
            temp_input = batch_global_x[i]
            temp_label = batch_label[i]

            # اگر داده/برچسب tuple یا list بود، عنصر اول دادهٔ اصلی است
            if isinstance(temp_input, (tuple, list)):
                temp_input = temp_input[0]
            if isinstance(temp_label, (tuple, list)):
                temp_label = temp_label[0]

            # تضمین نوع برچسب‌ها
            temp_label = temp_label.long()

            # شکل‌دهی ورودی مطابق منطق قبلی فایل
            x = temp_input                       # [S, T, D] یا مشابه
            x = torch.transpose(x, 1, 2)         # همان تبدیل‌های قدیمی
            x = torch.transpose(x * self.squence_weight, 1, 2)
            x = x.flatten(1)

            # AutoEncoder → z
            vae_loss, z = self.vae(x)            # z: [T, z_dim]

            # --- اصلاح اصلی: حذف softmax و کار با logits ---
            logits = self.mlp(z)                 # [T, C] (logits)
            # self.criterion.weight = self.criterion.weight.to(logits.device)
            accuarcy = torch.eq(logits.argmax(dim=1), temp_label).float().mean()
            classfier_loss = self.criterion(logits, temp_label)

            total_classfier_loss.append(classfier_loss)
            total_vae_loss.append(vae_loss)
            total_classfier_acc.append(accuarcy)

            # پدینگ z تا n_steps روی همان device
            T = z.shape[0]
            if T < self.n_steps:
                pad = torch.zeros(self.n_steps - T, self.z_dim,
                                  dtype=torch.float32, requires_grad=False, device=z.device)
                z_padded = torch.cat([z, pad], dim=0)
            else:
                z_padded = z[: self.n_steps]
            batch_z.append(z_padded)

        batch_z = torch.stack(batch_z)
        total_classfier_loss = torch.mean(torch.stack(total_classfier_loss))
        total_classfier_acc = torch.mean(torch.stack(total_classfier_acc))
        total_vae_loss = torch.mean(torch.stack(total_vae_loss))

        return total_vae_loss + total_classfier_loss, total_classfier_loss, total_classfier_acc, batch_z

