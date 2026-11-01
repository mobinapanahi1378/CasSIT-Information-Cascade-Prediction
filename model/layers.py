import torch
import torch.nn as nn
import torch.nn.init as init


class BiGCN(torch.nn.Module):
    def __init__(self, input_features, hidden_features, output_features):
        super(BiGCN, self).__init__()
        self.gcn1 = CheBy_conv(input_features, hidden_features)
        self.gcn2 = CheBy_conv(input_features + hidden_features, output_features)
        self.relu = nn.ReLU()

    def forward(self, x, L):
        x1 = self.relu(self.gcn1(x, L))
        x_ = torch.cat([x, x1], dim=-1)
        x_temp = self.relu(self.gcn2(x_, L))
        return x_temp


class MPL_Net(torch.nn.Module):
    def __init__(self, dens_hiddensize1, dens_hiddensize2, dens_inputsize, dens_outputsize, dens_dropout=0):
        super(MPL_Net, self).__init__()
        self.inputsize = dens_inputsize
        self.dens_hiddensize1 = dens_hiddensize1
        self.dens_hiddensize2 = dens_hiddensize2
        self.dens_dropout = dens_dropout
        self.outputsize = dens_outputsize
        self.setup_layers()

    def setup_layers(self):
        self.dens_net = torch.nn.Sequential(
            torch.nn.Linear(self.inputsize, self.dens_hiddensize1),
            torch.nn.ReLU(True),
            torch.nn.Dropout(p=self.dens_dropout),
            torch.nn.Linear(self.dens_hiddensize1, self.dens_hiddensize2),
            torch.nn.ReLU(True),
            torch.nn.Dropout(p=self.dens_dropout),
            torch.nn.Linear(self.dens_hiddensize2, self.outputsize)
        )

    def forward(self, x):
        return self.dens_net(x)


class CheBy_conv(torch.nn.Module):
    def __init__(self, input_dim, output_dim, use_bias=True):
        super(CheBy_conv, self).__init__()
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.use_bias = use_bias
        self.weight = nn.Parameter(torch.Tensor(input_dim, output_dim), requires_grad=True)
        if self.use_bias:
            self.bias = nn.Parameter(torch.Tensor(output_dim), requires_grad=True)
        else:
            self.register_parameter('bias', None)
        # self.reset_parameters()

    def reset_parameters(self):
        init.xavier_normal_(self.weight)
        if self.use_bias:
            init.uniform_(self.bias)

    def forward(self, x, lap):

        support = torch.matmul(x, self.weight)
        output = torch.matmul(lap.unsqueeze(1), support)
        if self.bias is not None:
            return output + self.bias
        else:
            return output

# import torch
# import torch.nn as nn
# import torch.nn.init as init


# class BiGCN(torch.nn.Module):
#     def __init__(self, input_features, hidden_features, output_features):
#         super(BiGCN, self).__init__()
#         self.gcn1 = CheBy_conv(input_features, hidden_features)
#         self.gcn2 = CheBy_conv(input_features + hidden_features, output_features)
#         self.relu = nn.ReLU()

#     def forward(self, x, L):
#         x1 = self.relu(self.gcn1(x, L))
#         x_ = torch.cat([x, x1], dim=-1)
#         x_temp = self.relu(self.gcn2(x_, L))
#         return x_temp


# class MPL_Net(torch.nn.Module):
#     def __init__(self, dens_hiddensize1, dens_hiddensize2, dens_inputsize, dens_outputsize, dens_dropout=0):
#         super(MPL_Net, self).__init__()
#         self.inputsize = dens_inputsize
#         self.dens_hiddensize1 = dens_hiddensize1
#         self.dens_hiddensize2 = dens_hiddensize2
#         self.dens_dropout = dens_dropout
#         self.outputsize = dens_outputsize
#         self.setup_layers()

#     def setup_layers(self):
#         self.dens_net = torch.nn.Sequential(
#             torch.nn.Linear(self.inputsize, self.dens_hiddensize1),
#             torch.nn.ReLU(True),
#             torch.nn.Dropout(p=self.dens_dropout),
#             torch.nn.Linear(self.dens_hiddensize1, self.dens_hiddensize2),
#             torch.nn.ReLU(True),
#             torch.nn.Dropout(p=self.dens_dropout),
#             torch.nn.Linear(self.dens_hiddensize2, self.outputsize)
#         )

#     def forward(self, x):
#         return torch.relu(self.dens_net(x))
#         # return torch.relu(self.dens_net(x))


# class CheBy_conv(torch.nn.Module):
#     def __init__(self, input_dim, output_dim, use_bias=True):
#         super(CheBy_conv, self).__init__()
#         self.input_dim = input_dim
#         self.output_dim = output_dim
#         self.use_bias = use_bias
#         self.weight = nn.Parameter(torch.Tensor(input_dim, output_dim), requires_grad=True)
#         if self.use_bias:
#             self.bias = nn.Parameter(torch.Tensor(output_dim), requires_grad=True)
#         else:
#             self.register_parameter('bias', None)
#         # self.reset_parameters()

#     def reset_parameters(self):
#         init.xavier_normal_(self.weight)
#         if self.use_bias:
#             init.uniform_(self.bias)

#     def forward(self, x, lap):

#         support = torch.matmul(x, self.weight)
#         output = torch.matmul(lap.unsqueeze(1), support)
#         if self.bias is not None:
#             return output + self.bias
#         else:
#             return output

# import torch
# import torch.nn as nn
# import torch.nn.init as init


# class BiGCN(torch.nn.Module):
#     def __init__(self, input_features, hidden_features, output_features):
#         super(BiGCN, self).__init__()
#         self.gcn1 = CheBy_conv(input_features, hidden_features)
#         self.gcn2 = CheBy_conv(input_features + hidden_features, output_features)
#         self.relu = nn.ReLU()

#     def forward(self, x, L):
#         x1 = self.relu(self.gcn1(x, L))
#         x_ = torch.cat([x, x1], dim=-1)
#         x_temp = self.relu(self.gcn2(x_, L))
#         return x_temp


# class MPL_Net(torch.nn.Module):
#     def __init__(self, dens_hiddensize1, dens_hiddensize2, dens_inputsize, dens_outputsize, dens_dropout=0):
#         super(MPL_Net, self).__init__()
#         self.inputsize = dens_inputsize
#         self.dens_hiddensize1 = dens_hiddensize1
#         self.dens_hiddensize2 = dens_hiddensize2
#         self.dens_dropout = dens_dropout
#         self.outputsize = dens_outputsize
#         self.setup_layers()

#     def setup_layers(self):
#         self.dens_net = torch.nn.Sequential(
#             torch.nn.Linear(self.inputsize, self.dens_hiddensize1),
#             torch.nn.ReLU(True),
#             torch.nn.Dropout(p=self.dens_dropout),
#             torch.nn.Linear(self.dens_hiddensize1, self.dens_hiddensize2),
#             torch.nn.ReLU(True),
#             torch.nn.Dropout(p=self.dens_dropout),
#             torch.nn.Linear(self.dens_hiddensize2, self.outputsize)
#         )

#     def forward(self, x):
#         return self.dens_net(x)


# class CheBy_conv(torch.nn.Module):
#     def __init__(self, input_dim, output_dim, use_bias=True):
#         super(CheBy_conv, self).__init__()
#         self.input_dim = input_dim
#         self.output_dim = output_dim
#         self.use_bias = use_bias
#         self.weight = nn.Parameter(torch.Tensor(input_dim, output_dim), requires_grad=True)
#         if self.use_bias:
#             self.bias = nn.Parameter(torch.Tensor(output_dim), requires_grad=True)
#         else:
#             self.register_parameter('bias', None)
#         # self.reset_parameters()

#     def reset_parameters(self):
#         init.xavier_normal_(self.weight)
#         if self.use_bias:
#             init.uniform_(self.bias)

#     def forward(self, x, lap):

#         support = torch.matmul(x, self.weight)
#         output = torch.matmul(lap.unsqueeze(1), support)
#         if self.bias is not None:
#             return output + self.bias
#         else:
#             return output

# attention pooling
# import torch
# import torch.nn as nn
# import torch.nn.init as init


# class BiGCN(torch.nn.Module):
#     def __init__(self, input_features, hidden_features, output_features):
#         super(BiGCN, self).__init__()
#         self.gcn1 = CheBy_conv(input_features, hidden_features)
#         self.gcn2 = CheBy_conv(input_features + hidden_features, output_features)
#         self.relu = nn.ReLU()

#     def forward(self, x, L):
#         """
#         x:  [B, N, F_in]
#         L:  [B, N, N] یا [N, N] (با broadcast)
#         خروجی: [B, T, N, F_out] در سناریوی شما (روی batch_x, batch_l)
#         """
#         x1 = self.relu(self.gcn1(x, L))          # [B, N, H]
#         x_ = torch.cat([x, x1], dim=-1)          # [B, N, F_in + H]
#         x_temp = self.relu(self.gcn2(x_, L))     # [B, N, F_out]
#         return x_temp


# class MPL_Net(torch.nn.Module):
#     def __init__(self, dens_hiddensize1, dens_hiddensize2,
#                  dens_inputsize, dens_outputsize, dens_dropout=0):
#         super(MPL_Net, self).__init__()
#         self.inputsize = dens_inputsize
#         self.dens_hiddensize1 = dens_hiddensize1
#         self.dens_hiddensize2 = dens_hiddensize2
#         self.dens_dropout = dens_dropout
#         self.outputsize = dens_outputsize
#         self.setup_layers()

#     def setup_layers(self):
#         self.dens_net = torch.nn.Sequential(
#             torch.nn.Linear(self.inputsize, self.dens_hiddensize1),
#             torch.nn.ReLU(True),
#             torch.nn.Dropout(p=self.dens_dropout),
#             torch.nn.Linear(self.dens_hiddensize1, self.dens_hiddensize2),
#             torch.nn.ReLU(True),
#             torch.nn.Dropout(p=self.dens_dropout),
#             torch.nn.Linear(self.dens_hiddensize2, self.outputsize)
#         )

#     def forward(self, x):
#         return torch.relu(self.dens_net(x))


# class CheBy_conv(torch.nn.Module):
#     def __init__(self, input_dim, output_dim, use_bias=True):
#         super(CheBy_conv, self).__init__()
#         self.input_dim = input_dim
#         self.output_dim = output_dim
#         self.use_bias = use_bias
#         self.weight = nn.Parameter(
#             torch.Tensor(input_dim, output_dim), requires_grad=True
#         )
#         if self.use_bias:
#             self.bias = nn.Parameter(
#                 torch.Tensor(output_dim), requires_grad=True
#             )
#         else:
#             self.register_parameter('bias', None)
#         # self.reset_parameters()

#     def reset_parameters(self):
#         init.xavier_normal_(self.weight)
#         if self.use_bias:
#             init.uniform_(self.bias)

#     def forward(self, x, lap):
#         """
#         x:   [B, N, F_in]
#         lap: [B, N, N] یا [N, N] (با broadcast)
#         """
#         support = torch.matmul(x, self.weight)          # [B, N, F_out]
#         output = torch.matmul(lap.unsqueeze(1), support)  # [B, 1, N, F_out] → broadcast
#         if self.bias is not None:
#             return output + self.bias
#         else:
#             return output


# class NodeAttentionPooling(nn.Module):
#     """
#     Attention pooling روی بعد نودها بعد از GCN.

#     ورودی:
#         x: [B, T, N, F]  (batch, snapshot, node, feature)

#     خروجی:
#         out:   [B, T, F]      نماینده‌ی هر snapshot
#         alpha: [B, T, N, 1]   وزن attention هر نود
#     """
#     def __init__(self, in_dim: int):
#         super(NodeAttentionPooling, self).__init__()
#         self.proj = nn.Linear(in_dim, in_dim)
#         self.score = nn.Linear(in_dim, 1)

#     def forward(self, x, mask=None):
#         """
#         x:    [B, T, N, F]
#         mask: [B, T, N] (اختیاری، ۱=نود واقعی، ۰=padding)
#         """
#         # مرحله ۱: تبدیل ویژگی و حساب نمره attention
#         # h: [B, T, N, F]
#         h = torch.tanh(self.proj(x))

#         # e: [B, T, N, 1]
#         e = self.score(h)

#         if mask is not None:
#             # نودهای padding را به -inf بفرست تا وزن نگیرند
#             e = e.masked_fill(mask.unsqueeze(-1) == 0, -1e9)

#         # مرحله ۲: softmax روی محور نودها
#         # alpha: [B, T, N, 1]
#         alpha = torch.softmax(e, dim=2)

#         # مرحله ۳: جمع وزن‌دار روی نودها
#         # out: [B, T, F]
#         out = (alpha * x).sum(dim=2)

#         return out, alpha



# import torch
# import torch.nn as nn
# import torch.nn.init as init
# import torch.nn.functional as F


# class BiGCN(torch.nn.Module):
#     def __init__(self, input_features, hidden_features, output_features):
#         super(BiGCN, self).__init__()
#         self.gcn1 = CheBy_conv(input_features, hidden_features)
#         self.gcn2 = CheBy_conv(input_features + hidden_features, output_features)
#         self.relu = nn.ReLU()

#     def forward(self, x, L):
#         x1 = self.relu(self.gcn1(x, L))
#         x_ = torch.cat([x, x1], dim=-1)
#         x_temp = self.relu(self.gcn2(x_, L))
#         return x_temp


# class MPL_Net(nn.Module):
#     """
#     MLP با فعال‌ساز نهایی اختیاری.
#     - final_activation="relu": مثل نسخهٔ قبلی رفتار می‌کند.
#     - final_activation="none": logits خام برمی‌گرداند (برای CrossEntropyLoss).
#     """
#     def __init__(
#         self,
#         dens_inputsize: int,
#         dens_outputsize: int,
#         dens_dropout: float = 0.0,
#         dens_hiddensize1: int = 128,
#         dens_hiddensize2: int = 64,
#         final_activation: str = "relu",
#     ):
#         super(MPL_Net, self).__init__()
#         assert final_activation in ("relu", "none"), \
#             "final_activation must be 'relu' or 'none'"
#         self.final_activation = final_activation

#         self.dens_net = nn.Sequential(
#             nn.Linear(dens_inputsize, dens_hiddensize1),
#             nn.ReLU(),
#             nn.Dropout(dens_dropout),
#             nn.Linear(dens_hiddensize1, dens_hiddensize2),
#             nn.ReLU(),
#             nn.Dropout(dens_dropout),
#             nn.Linear(dens_hiddensize2, dens_outputsize),
#         )

#     def forward(self, x: torch.Tensor) -> torch.Tensor:
#         x = self.dens_net(x)
#         if self.final_activation == "relu":
#             x = F.relu(x)
#         # اگر "none" باشد، همان logits خام برمی‌گردد
#         return x

# class CheBy_conv(torch.nn.Module):
#     def __init__(self, input_dim, output_dim, use_bias=True):
#         super(CheBy_conv, self).__init__()
#         self.input_dim = input_dim
#         self.output_dim = output_dim
#         self.use_bias = use_bias
#         self.weight = nn.Parameter(torch.Tensor(input_dim, output_dim), requires_grad=True)
#         if self.use_bias:
#             self.bias = nn.Parameter(torch.Tensor(output_dim), requires_grad=True)
#         else:
#             self.register_parameter('bias', None)
#         # self.reset_parameters()

#     def reset_parameters(self):
#         init.xavier_normal_(self.weight)
#         if self.use_bias:
#             init.uniform_(self.bias)

#     def forward(self, x, lap):

#         support = torch.matmul(x, self.weight)
#         output = torch.matmul(lap.unsqueeze(1), support)
#         if self.bias is not None:
#             return output + self.bias
#         else:
#             return output
