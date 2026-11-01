import networkx as nx
import pickle
import time
import random

max_nodes = 50
nei_num = "2nei"
data_type = 'twitter'
random.seed(0)


def find123Nei(G, node):
    nei1_li = {}
    nei2_li = {}
    nei3_li = {}
    nei4_li = {}
    nei5_li = {}
    nei6_li = {}
    for FNs in random.sample(list(nx.neighbors(G, node)),
                             min(max_nodes, len(list(nx.neighbors(G, node))))):  # find 1_th neighbors
        nei1_li[FNs] = nx.degree(G, FNs)
    if nei2_li.__contains__(node):
        nei1_li.pop(node)
    if nei_num == "1nei":
        nei1_drgees = random.sample(list(nei1_li.values()), min(len(nei1_li), max_nodes))
        return nei1_drgees
    for n1 in nei1_li.keys():
        for SNs in random.sample(list(nx.neighbors(G, n1)),
                                 min(max_nodes // 2, len(list(nx.neighbors(G, n1))))):  # find 2_th neighbors
            nei2_li[SNs] = nx.degree(G, SNs)
    [nei2_li.pop(n) for n in list(nei1_li.keys()) + [node] if nei2_li.__contains__(n)]
    if nei_num == "2nei":
        nei1_drgees = random.sample(list(nei1_li.values()), min(len(nei1_li), max_nodes))
        nei2_drgees = random.sample(list(nei2_li.values()), min(len(nei2_li), max_nodes))
        return nei1_drgees, nei2_drgees
    elif nei_num == "3nei":
        for n2 in nei2_li.keys():
            for TNs in random.sample(list(nx.neighbors(G, n2)), min(max_nodes // 4, len(list(nx.neighbors(G, n2))))):
                nei3_li[TNs] = nx.degree(G, TNs)
        [nei3_li.pop(n) for n in list(nei1_li.keys()) + list(nei2_li.keys()) + [node] if nei3_li.__contains__(n)]
        nei1_drgees = random.sample(list(nei1_li.values()), min(len(nei1_li), max_nodes))
        nei2_drgees = random.sample(list(nei2_li.values()), min(len(nei2_li), max_nodes))
        nei3_drgees = random.sample(list(nei3_li.values()), min(len(nei3_li), max_nodes))
        return nei1_drgees, nei2_drgees, nei3_drgees
    elif nei_num == "4nei":
        for n2 in nei2_li.keys():
            for TNs in random.sample(list(nx.neighbors(G, n2)), min(max_nodes // 4, len(list(nx.neighbors(G, n2))))):
                nei3_li[TNs] = nx.degree(G, TNs)
        [nei3_li.pop(n) for n in list(nei1_li.keys()) + list(nei2_li.keys()) + [node] if nei3_li.__contains__(n)]
        for n3 in nei3_li.keys():
            for FNs in random.sample(list(nx.neighbors(G, n3)), min(max_nodes // 8, len(list(nx.neighbors(G, n3))))):
                nei4_li[FNs] = nx.degree(G, FNs)
        [nei4_li.pop(n) for n in list(nei1_li.keys()) + list(nei2_li.keys()) + list(nei3_li.keys()) + [node] if
         nei4_li.__contains__(n)]
        nei1_drgees = random.sample(list(nei1_li.values()), min(len(nei1_li), max_nodes))
        nei2_drgees = random.sample(list(nei2_li.values()), min(len(nei2_li), max_nodes))
        nei3_drgees = random.sample(list(nei3_li.values()), min(len(nei3_li), max_nodes))
        nei4_drgees = random.sample(list(nei4_li.values()), min(len(nei4_li), max_nodes))
        return nei1_drgees, nei2_drgees, nei3_drgees, nei4_drgees
    elif nei_num == '5nei':
        for n2 in nei2_li.keys():
            for TNs in random.sample(list(nx.neighbors(G, n2)), min(max_nodes // 4, len(list(nx.neighbors(G, n2))))):
                nei3_li[TNs] = nx.degree(G, TNs)
        [nei3_li.pop(n) for n in list(nei1_li.keys()) + list(nei2_li.keys()) + [node] if nei3_li.__contains__(n)]
        for n3 in nei3_li.keys():
            for FNs in random.sample(list(nx.neighbors(G, n3)), min(max_nodes // 8, len(list(nx.neighbors(G, n3))))):
                nei4_li[FNs] = nx.degree(G, FNs)
        [nei4_li.pop(n) for n in list(nei1_li.keys()) + list(nei2_li.keys()) + list(nei3_li.keys()) + [node] if
         nei4_li.__contains__(n)]
        for n4 in nei4_li.keys():
            for FFNs in random.sample(list(nx.neighbors(G, n4)), min(max_nodes // 16, len(list(nx.neighbors(G, n4))))):
                nei5_li[FFNs] = nx.degree(G, FFNs)
        [nei5_li.pop(n) for n in
         list(nei1_li.keys()) + list(nei2_li.keys()) + list(nei3_li.keys()) + list(nei4_li.keys()) + [node] if
         nei5_li.__contains__(n)]
        nei1_drgees = random.sample(list(nei1_li.values()), min(len(nei1_li), max_nodes))
        nei2_drgees = random.sample(list(nei2_li.values()), min(len(nei2_li), max_nodes))
        nei3_drgees = random.sample(list(nei3_li.values()), min(len(nei3_li), max_nodes))
        nei4_drgees = random.sample(list(nei4_li.values()), min(len(nei4_li), max_nodes))
        nei5_drgees = random.sample(list(nei5_li.values()), min(len(nei5_li), max_nodes))
        return nei1_drgees, nei2_drgees, nei3_drgees, nei4_drgees, nei5_drgees
    elif nei_num == '6nei':
        for n2 in nei2_li.keys():
            for TNs in random.sample(list(nx.neighbors(G, n2)), min(max_nodes // 4, len(list(nx.neighbors(G, n2))))):
                nei3_li[TNs] = nx.degree(G, TNs)
        [nei3_li.pop(n) for n in list(nei1_li.keys()) + list(nei2_li.keys()) + [node] if nei3_li.__contains__(n)]
        for n3 in nei3_li.keys():
            for FNs in random.sample(list(nx.neighbors(G, n3)), min(max_nodes // 8, len(list(nx.neighbors(G, n3))))):
                nei4_li[FNs] = nx.degree(G, FNs)
        [nei4_li.pop(n) for n in list(nei1_li.keys()) + list(nei2_li.keys()) + list(nei3_li.keys()) + [node] if
         nei4_li.__contains__(n)]
        for n4 in nei4_li.keys():
            for FFNs in random.sample(list(nx.neighbors(G, n4)), min(max_nodes // 16, len(list(nx.neighbors(G, n4))))):
                nei5_li[FFNs] = nx.degree(G, FFNs)
        [nei5_li.pop(n) for n in
         list(nei1_li.keys()) + list(nei2_li.keys()) + list(nei3_li.keys()) + list(nei4_li.keys()) + [node] if
         nei5_li.__contains__(n)]
        for n5 in nei5_li.keys():
            for SSNs in random.sample(list(nx.neighbors(G, n5)), min(max_nodes // 16, len(list(nx.neighbors(G, n5))))):
                nei6_li[SSNs] = nx.degree(G, SSNs)
        [nei6_li.pop(n) for n in
         list(nei1_li.keys()) + list(nei2_li.keys()) + list(nei3_li.keys()) + list(nei4_li.keys()) + list(
             nei5_li.keys()) + [node] if nei6_li.__contains__(n)]

        nei1_drgees = random.sample(list(nei1_li.values()), min(len(nei1_li), max_nodes))
        nei2_drgees = random.sample(list(nei2_li.values()), min(len(nei2_li), max_nodes))
        nei3_drgees = random.sample(list(nei3_li.values()), min(len(nei3_li), max_nodes))
        nei4_drgees = random.sample(list(nei4_li.values()), min(len(nei4_li), max_nodes))
        nei5_drgees = random.sample(list(nei5_li.values()), min(len(nei5_li), max_nodes))
        nei6_drgees = random.sample(list(nei6_li.values()), min(len(nei6_li), max_nodes))
        return nei1_drgees, nei2_drgees, nei3_drgees, nei4_drgees, nei5_drgees, nei6_drgees


gg_path = 'C:\\Users\\nit\\Desktop\\CasCIFF-master\\CasCIFF-master-pro\\dataset\\CasCIFF\\{}\\global\\global_graph.pkl'.format(data_type)
global_emb = 'C:\\Users\\nit\\Desktop\\CasCIFF-master\\CasCIFF-master-pro\\dataset\\CasCIFF\\{0}\\global\\global_emb_{1}_sample{2}.txt'.format(data_type, nei_num,
                                                                                             max_nodes)
with open(gg_path, 'rb') as f:
    gg = pickle.load(f)
nodes = list(nx.nodes(gg))
total_count = len(nodes)
count = 0
f = open(global_emb, 'w')
start_time = time.time()
for node in nodes:
    neighbors = find123Nei(gg, node)
    if nei_num == "1nei":
        line = node + '\t' + ' '.join([str(x) for x in sorted(neighbors, reverse=True)]) + '\t' + str(
            nx.degree(gg, node)) + '\n'
    elif nei_num == "2nei":
        line = node + '\t' + ' '.join([str(x) for x in sorted(neighbors[0], reverse=True)]) + '\t' + ' '.join(
            [str(x) for x in sorted(neighbors[1], reverse=True)]) + '\t' + str(nx.degree(gg, node)) + '\n'
    elif nei_num == "3nei":
        line = node + '\t' + ' '.join([str(x) for x in sorted(neighbors[0], reverse=True)]) + '\t' + ' '.join(
            [str(x) for x in sorted(neighbors[1], reverse=True)]) + '\t' + ' '.join(
            [str(x) for x in sorted(neighbors[2], reverse=True)]) + '\t' + str(nx.degree(gg, node)) + '\n'
    elif nei_num == "4nei":
        line = node + '\t' + ' '.join(
            [str(x) for x in sorted(neighbors[0], reverse=True)]) + '\t' + ' '.join(
            [str(x) for x in sorted(neighbors[1], reverse=True)]) + '\t' + ' '.join(
            [str(x) for x in sorted(neighbors[2], reverse=True)]) + '\t' + ' '.join(
            [str(x) for x in sorted(neighbors[3], reverse=True)]) + '\t' + str(nx.degree(gg, node)) + '\n'
    elif nei_num == "5nei":
        line = node + '\t' + ' '.join(
            [str(x) for x in sorted(neighbors[0], reverse=True)]) + '\t' + ' '.join(
            [str(x) for x in sorted(neighbors[1], reverse=True)]) + '\t' + ' '.join(
            [str(x) for x in sorted(neighbors[2], reverse=True)]) + '\t' + ' '.join(
            [str(x) for x in sorted(neighbors[3], reverse=True)]) + '\t' + ' '.join(
            [str(x) for x in sorted(neighbors[4], reverse=True)]) + '\t' + str(nx.degree(gg, node)) + '\n'
    elif nei_num == "6nei":
        line = node + '\t' + ' '.join(
            [str(x) for x in sorted(neighbors[0], reverse=True)]) + '\t' + ' '.join(
            [str(x) for x in sorted(neighbors[1], reverse=True)]) + '\t' + ' '.join(
            [str(x) for x in sorted(neighbors[2], reverse=True)]) + '\t' + ' '.join(
            [str(x) for x in sorted(neighbors[3], reverse=True)]) + '\t' + ' '.join(
            [str(x) for x in sorted(neighbors[4], reverse=True)]) + '\t' + ' '.join(
            [str(x) for x in sorted(neighbors[5], reverse=True)]) + '\t' + str(nx.degree(gg, node)) + '\n'
    f.write(line)
    count += 1
    if count % 10000 == 0:
        print('has processed {}/{} time:{:.2f}s'.format(count, total_count, time.time() - start_time))
        start_time = time.time()
f.close()






# import networkx as nx
# import pickle
# import time
# import random

# max_nodes = 50
# nei_num = "2nei"
# data_type = 'twitter'
# random.seed(0)

# def find123Nei(G, node):
#     # این تابع فقط ساختار همسایه‌ها (1–6-هاپ) را برمی‌گرداند؛
#     # مقادیر فیچر (PageRank) را خارج از این تابع می‌خوانیم.
#     nei1 = set()
#     nei2 = set()
#     nei3 = set()
#     nei4 = set()
#     nei5 = set()
#     nei6 = set()

#     # 1-hop
#     n1_all = list(nx.neighbors(G, node))
#     n1_pick = random.sample(n1_all, min(max_nodes, len(n1_all)))
#     nei1.update(n1_pick)

#     if nei_num == "1nei":
#         return [list(nei1)]

#     # 2-hop
#     for n1 in nei1:
#         n2_all = list(nx.neighbors(G, n1))
#         n2_pick = random.sample(n2_all, min(max_nodes // 2, len(n2_all)))
#         nei2.update(n2_pick)
#     nei2 -= (nei1 | {node})
#     if nei_num == "2nei":
#         return [list(nei1), list(nei2)]

#     # 3-hop
#     for n2 in list(nei2):
#         n3_all = list(nx.neighbors(G, n2))
#         n3_pick = random.sample(n3_all, min(max_nodes // 4, len(n3_all)))
#         nei3.update(n3_pick)
#     nei3 -= (nei1 | nei2 | {node})
#     if nei_num == "3nei":
#         return [list(nei1), list(nei2), list(nei3)]

#     # 4-hop
#     for n3 in list(nei3):
#         n4_all = list(nx.neighbors(G, n3))
#         n4_pick = random.sample(n4_all, min(max_nodes // 8, len(n4_all)))
#         nei4.update(n4_pick)
#     nei4 -= (nei1 | nei2 | nei3 | {node})
#     if nei_num == "4nei":
#         return [list(nei1), list(nei2), list(nei3), list(nei4)]

#     # 5-hop
#     for n4 in list(nei4):
#         n5_all = list(nx.neighbors(G, n4))
#         n5_pick = random.sample(n5_all, min(max_nodes // 16, len(n5_all)))
#         nei5.update(n5_pick)
#     nei5 -= (nei1 | nei2 | nei3 | nei4 | {node})
#     if nei_num == "5nei":
#         return [list(nei1), list(nei2), list(nei3), list(nei4), list(nei5)]

#     # 6-hop
#     for n5 in list(nei5):
#         n6_all = list(nx.neighbors(G, n5))
#         n6_pick = random.sample(n6_all, min(max_nodes // 16, len(n6_all)))
#         nei6.update(n6_pick)
#     nei6 -= (nei1 | nei2 | nei3 | nei4 | nei5 | {node})
#     return [list(nei1), list(nei2), list(nei3), list(nei4), list(nei5), list(nei6)]


# gg_path = 'C:\\Users\\nit\\Desktop\\CasCIFF-master\\CasCIFF-master-pro\\dataset\\CasCIFF\\{}\\global\\global_graph.pkl'.format(data_type)
# global_emb = 'C:\\Users\\nit\\Desktop\\CasCIFF-master\\CasCIFF-master-pro\\dataset\\CasCIFF\\{0}\\global\\global_emb_{1}_sample{2}.txt'.format(
#     data_type, nei_num, max_nodes
# )

# with open(gg_path, 'rb') as f:
#     gg = pickle.load(f)

# nodes = list(nx.nodes(gg))
# total_count = len(nodes)
# count = 0

# # --- تغییر کلیدی: محاسبهٔ PageRank یک‌بار روی گراف ---
# # توجه: alpha (دمپینگ) را می‌توانید تنظیم کنید.
# pagerank = nx.pagerank(gg, alpha=0.85, max_iter=100)

# f = open(global_emb, 'w')
# start_time = time.time()
# for node in nodes:
#     # فهرست همسایه‌ها در عمق‌های مختلف (بدون مقدار)
#     nei_levels = find123Nei(gg, node)

#     # برای هر سطح، مقدار PR همسایه‌ها را برداشته، مرتب، و تا max_nodes پد می‌کنیم
#     pr_levels = []
#     for level_nodes in nei_levels:
#         pr_vals = [pagerank.get(n, 0.0) for n in level_nodes]
#         pr_vals_sorted = sorted(pr_vals, reverse=True)
#         if len(pr_vals_sorted) > max_nodes:
#             pr_vals_sorted = pr_vals_sorted[:max_nodes]
#         else:
#             pr_vals_sorted += [0.0] * (max_nodes - len(pr_vals_sorted))
#         pr_levels.append(pr_vals_sorted)

#     # مقدار PR خود نود را به‌عنوان «فیلد آخر» می‌نویسیم (قبلاً degree بود)
#     node_pr = pagerank.get(node, 0.0)

#     # ساخت خط خروجی مشابه نسخهٔ درجه‌محور، اما با PR
#     parts = [node]
#     for arr in pr_levels:
#         parts.append(' '.join(f'{v:.8f}' for v in arr))
#     parts.append(f'{node_pr:.8f}')
#     line = '\t'.join(parts) + '\n'
#     f.write(line)

#     count += 1
#     if count % 10000 == 0:
#         print('has processed {}/{} time:{:.2f}s'.format(count, total_count, time.time() - start_time))
#         start_time = time.time()

# f.close()

