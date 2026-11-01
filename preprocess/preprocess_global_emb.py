import pickle
import time

start = time.time()
max_nodes = 50
node_level = {}
data_type = 'twitter'
interval = '\\2day'
isordered = '2nei_sample{}'.format(max_nodes)
Data_Base = 'C:\\Users\\nit\\Desktop\\CasCIFF-master\\CasCIFF-master-pro\\dataset\\CasCIFF\\' + data_type
Data_path = 'C:\\Users\\nit\\Desktop\\CasCIFF-master\\CasCIFF-master-pro\\dataset\\CasCIFF\\{0}\\global\\global_emb_'.format(data_type) + isordered + '.txt'
with open(Data_path, 'r') as f:
    for line in f:
        parts = line.rstrip('\n').split('\t')
        node_level[parts[0]] = int(parts[-1])
a = sorted(node_level.items(), key=lambda x: x[1], reverse=True)
'''
Experiment:
    Two categories: important people/non-important people
    Initial classification index: Top 30%
'''
save_file = Data_Base + interval
node_class = {}
count = 0
top = 30
for node in a:
    if count < len(a) // top:
        node_class[node[0]] = 1
    else:
        node_class[node[0]] = 0
    count += 1
# Node embedding
node_emb = {}
print('start process generate data...')
with open(Data_path, 'r') as f:
    for line in f:
        parts = line.rstrip('\n').split('\t')
        node_id = parts[0]
        node_features = []
        negF_degrees = []
        negS_degrees = []
        negT_degrees = []
        negV_degrees = []
        negVV_degrees = []
        negSS_degrees = []
        if isordered.__contains__("0nei"):
            if not node_emb.__contains__(node_id):
                drgree = parts[-1]
                if degree != '':
                    node_emb[node_id] = int(degree)
            continue
        length = 0
        for degree in parts[1].split(' '):
            if degree == '':
                continue
            negF_degrees.append(int(degree))
            length += 1
        while length < max_nodes:
            negF_degrees.append(0)
            length += 1
        node_features.append(negF_degrees)
        if isordered.__contains__("1nei"):
            if not node_emb.__contains__(node_id):
                node_emb[node_id] = node_features
            continue
        length = 0
        for degree in parts[2].split(' '):
            if degree == '':
                continue
            negS_degrees.append(int(degree))
            length += 1
        while length < max_nodes:
            negS_degrees.append(0)
            length += 1
        node_features.append(negS_degrees)
        if isordered.__contains__("2nei"):
            if not node_emb.__contains__(node_id):
                node_emb[node_id] = node_features
            continue
        length = 0
        for degree in parts[3].split(' '):
            if degree == '':
                continue
            negT_degrees.append(int(degree))
            length += 1
        while length < max_nodes:
            negT_degrees.append(0)
            length += 1
        node_features.append(negT_degrees)
        if isordered.__contains__("3nei"):
            if not node_emb.__contains__(node_id):
                node_emb[node_id] = node_features
            continue
        length = 0
        for degree in parts[4].split(' '):
            if degree == '':
                continue
            negV_degrees.append(int(degree))
            length += 1
        while length < max_nodes:
            negV_degrees.append(0)
            length += 1
        node_features.append(negV_degrees)
        if isordered.__contains__("4nei"):
            if not node_emb.__contains__(node_id):
                node_emb[node_id] = node_features
            continue
        length = 0
        for degree in parts[5].split(' '):
            if degree == '':
                continue
            negVV_degrees.append(int(degree))
            length += 1
        while length < max_nodes:
            negVV_degrees.append(0)
            length += 1
        node_features.append(negVV_degrees)
        if isordered.__contains__("5nei"):
            if not node_emb.__contains__(node_id):
                node_emb[node_id] = node_features
            continue
        length = 0
        for degree in parts[6].split(' '):
            if degree == '':
                continue
            negSS_degrees.append(int(degree))
            length += 1
        while length < max_nodes:
            negSS_degrees.append(0)
            length += 1
        node_features.append(negSS_degrees)
        if not node_emb.__contains__(node_id):
            node_emb[node_id] = node_features

train_file = save_file + '\\shortestpath_train.txt'
test_file = save_file + '\\shortestpath_test.txt'
val_file = save_file + '\\shortestpath_val.txt'
print('start process train data...')

start_time = time.time()
count = 0
f = open(train_file, 'r')
total_count = len(f.readlines())
f.close()
with open(train_file, 'r') as f:
    x_data_train = []
    y_data_train = []
    for line in f:
        nodes = []
        parts = line.rstrip('\n').split('\t')
        for path in parts[1:]:
            path = path.split(':')
            t = int(path[-1])
            node = path[0].split(',')[-1]
            nodes.append((node, t))
        nodes.sort(key=lambda tup: tup[1])
        x_data = []
        y_data = []
        for i in range(min(len(nodes), 100)):
            node = nodes[i][0]
            x_data.append(node_emb[node])
            y_data.append(node_class[node])
        x_data_train.append(x_data)
        y_data_train.append(y_data)
        count += 1
        if count % 1000 == 0:
            print('has processed {}/{} time:{}s'.format(count, total_count, time.time() - start_time))
            start_time = time.time()
    pickle.dump((x_data_train, y_data_train),
                open(save_file + '/global_step_train_' + isordered + '_top_' + str(top) + '.pkl', 'wb'))

print('start process val data...')
start_time = time.time()
count = 0
f = open(val_file, 'r')
total_count = len(f.readlines())
f.close()
with open(val_file, 'r') as f:
    x_data_val = []
    y_data_val = []
    for line in f:
        nodes = []
        parts = line.rstrip('\n').split('\t')
        for path in parts[1:]:
            path = path.split(':')
            t = int(path[-1])
            node = path[0].split(',')[-1]
            nodes.append((node, t))
        nodes.sort(key=lambda tup: tup[1])
        x_data = []
        y_data = []
        for i in range(min(len(nodes), 100)):
            node = nodes[i][0]
            x_data.append(node_emb[node])
            y_data.append(node_class[node])
        x_data_val.append(x_data)
        y_data_val.append(y_data)
        count += 1
        if count % 1000 == 0:
            print('has processed {}/{} time:{}s'.format(count, total_count, time.time() - start_time))
            start_time = time.time()
    pickle.dump((x_data_val, y_data_val),
                open(save_file + '/global_step_val_' + isordered + '_top_' + str(top) + '.pkl', 'wb'))

print('start process test data...')
start_time = time.time()
count = 0
f = open(test_file, 'r')
total_count = len(f.readlines())
f.close()
with open(test_file, 'r') as f:
    x_data_test = []
    y_data_test = []
    for line in f:
        nodes = []
        parts = line.rstrip('\n').split('\t')
        for path in parts[1:]:
            path = path.split(':')
            t = int(path[-1])
            node = path[0].split(',')[-1]
            nodes.append((node, t))
        nodes.sort(key=lambda tup: tup[1])
        x_data = []
        y_data = []
        for i in range(min(len(nodes), 100)):
            node = nodes[i][0]
            x_data.append(node_emb[node])
            y_data.append(node_class[node])
        x_data_test.append(x_data)
        y_data_test.append(y_data)
        count += 1
        if count % 1000 == 0:
            print('has processed {}/{} time:{}s'.format(count, total_count, time.time() - start_time))
            start_time = time.time()
    pickle.dump((x_data_test, y_data_test),
                open(save_file + '/global_step_test_' + isordered + '_top_' + str(top) + '.pkl', 'wb'))

print('Finished!!!')
print('total time {}s'.format(time.time() - start))





# import pickle
# import time

# start = time.time()
# max_nodes = 50
# node_level = {}
# data_type = 'twitter'
# interval = '/2day'
# isordered = '2nei_sample{}'.format(max_nodes)
# Data_Base = 'C:\\Users\\nit\\Desktop\\CasCIFF-master\\CasCIFF-master-pro\\dataset\\CasCIFF\\' + data_type
# Data_path = 'C:\\Users\\nit\\Desktop\\CasCIFF-master\\CasCIFF-master-pro\\dataset\\CasCIFF\\{0}\\global\\global_emb_'.format(data_type) + isordered + '.txt'

# # --- تغییر کلیدی: لیبل‌گذاری بر اساس PageRank (آخرین ستون فایل) ---
# with open(Data_path, 'r') as f:
#     for line in f:
#         parts = line.rstrip('\n').split('\t')
#         # آخرین ستون: PR خود نود (float)
#         node_level[parts[0]] = float(parts[-1])

# # مرتب‌سازی نزولی براساس PageRank
# a = sorted(node_level.items(), key=lambda x: x[1], reverse=True)

# '''
# Experiment:
#     Two categories: important people / non-important people
#     Initial classification index: Top 30%  (براساس PageRank)
# '''
# save_file = Data_Base + interval
# node_class = {}
# count = 0
# top = 30  # یعنی Top 1/top
# for node in a:
#     if count < len(a) // top:
#         node_class[node[0]] = 1
#     else:
#         node_class[node[0]] = 0
#     count += 1

# # --- خواندن فیچرها: مقادیر PR همسایه‌ها (float)، با پدینگ 0.0 ---
# node_emb = {}
# print('start process generate data...')
# with open(Data_path, 'r') as f:
#     for line in f:
#         parts = line.rstrip('\n').split('\t')
#         node_id = parts[0]
#         node_features = []

#         if isordered.__contains__("0nei"):
#             if not node_emb.__contains__(node_id):
#                 node_pr = parts[-1]
#                 if node_pr != '':
#                     node_emb[node_id] = float(node_pr)
#             continue

#         # هر سطح همسایگی را به‌ترتیب بخوانیم: parts[1], parts[2], ...
#         # هرکدام max_nodes مقدار PR (float) دارند که احتمالا با صفر پد شده‌اند.
#         idx = 1
#         # 1-hop
#         pr_1 = []
#         for val in parts[idx].split(' '):
#             if val == '':
#                 continue
#             pr_1.append(float(val))
#         while len(pr_1) < max_nodes:
#             pr_1.append(0.0)
#         node_features.append(pr_1)
#         if isordered.__contains__("1nei"):
#             if not node_emb.__contains__(node_id):
#                 node_emb[node_id] = node_features
#             continue

#         # 2-hop
#         idx += 1
#         pr_2 = []
#         for val in parts[idx].split(' '):
#             if val == '':
#                 continue
#             pr_2.append(float(val))
#         while len(pr_2) < max_nodes:
#             pr_2.append(0.0)
#         node_features.append(pr_2)
#         if isordered.__contains__("2nei"):
#             if not node_emb.__contains__(node_id):
#                 node_emb[node_id] = node_features
#             continue

#         # 3-hop
#         idx += 1
#         pr_3 = []
#         for val in parts[idx].split(' '):
#             if val == '':
#                 continue
#             pr_3.append(float(val))
#         while len(pr_3) < max_nodes:
#             pr_3.append(0.0)
#         node_features.append(pr_3)
#         if isordered.__contains__("3nei"):
#             if not node_emb.__contains__(node_id):
#                 node_emb[node_id] = node_features
#             continue

#         # 4-hop
#         idx += 1
#         pr_4 = []
#         for val in parts[idx].split(' '):
#             if val == '':
#                 continue
#             pr_4.append(float(val))
#         while len(pr_4) < max_nodes:
#             pr_4.append(0.0)
#         node_features.append(pr_4)
#         if isordered.__contains__("4nei"):
#             if not node_emb.__contains__(node_id):
#                 node_emb[node_id] = node_features
#             continue

#         # 5-hop
#         idx += 1
#         pr_5 = []
#         for val in parts[idx].split(' '):
#             if val == '':
#                 continue
#             pr_5.append(float(val))
#         while len(pr_5) < max_nodes:
#             pr_5.append(0.0)
#         node_features.append(pr_5)
#         if isordered.__contains__("5nei"):
#             if not node_emb.__contains__(node_id):
#                 node_emb[node_id] = node_features
#             continue

#         # 6-hop
#         idx += 1
#         pr_6 = []
#         for val in parts[idx].split(' '):
#             if val == '':
#                 continue
#             pr_6.append(float(val))
#         while len(pr_6) < max_nodes:
#             pr_6.append(0.0)
#         node_features.append(pr_6)

#         if not node_emb.__contains__(node_id):
#             node_emb[node_id] = node_features

# train_file = save_file + '/shortestpath_train.txt'
# test_file = save_file + '/shortestpath_test.txt'
# val_file = save_file + '/shortestpath_val.txt'
# print('start process train data...')

# def _build_xy(file_path, out_pkl_path):
#     start_time = time.time()
#     count = 0
#     with open(file_path, 'r') as f:
#         total_count = len(f.readlines())
#     with open(file_path, 'r') as f:
#         x_data = []
#         y_data = []
#         for line in f:
#             nodes = []
#             parts = line.rstrip('\n').split('\t')
#             for path in parts[1:]:
#                 path = path.split(':')
#                 t = int(path[-1])
#                 node = path[0].split(',')[-1]
#                 nodes.append((node, t))
#             nodes.sort(key=lambda tup: tup[1])

#             xx = []
#             yy = []
#             for i in range(min(len(nodes), 100)):
#                 node = nodes[i][0]
#                 xx.append(node_emb[node])           # فیچرها: PR همسایه‌ها (float)
#                 yy.append(node_class[node])         # لیبل: Top-X% براساس PR
#             x_data.append(xx)
#             y_data.append(yy)

#             count += 1
#             if count % 1000 == 0:
#                 print('has processed {}/{} time:{:.2f}s'.format(count, total_count, time.time() - start_time))
#                 start_time = time.time()
#     pickle.dump((x_data, y_data), open(out_pkl_path, 'wb'))

# # train / val / test
# _build_xy(train_file, save_file + '/global_step_train_' + isordered + '_top_' + str(top) + '.pkl')
# print('start process val data...')
# _build_xy(val_file,   save_file + '/global_step_val_'   + isordered + '_top_' + str(top) + '.pkl')
# print('start process test data...')
# _build_xy(test_file,  save_file + '/global_step_test_'  + isordered + '_top_' + str(top) + '.pkl')

# print('Finished!!!')
# print('total time {}s'.format(time.time() - start))
