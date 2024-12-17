# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pOW0xjZbUgrHwuntmaowB9rZa2neNGYo
"""

# Import library
import networkx as nx
import matplotlib.pyplot as plt

# Inisialisasi graf
G = nx.Graph()

# List karyawan (nodes)
employees = ["bulan", "ayu", "yohani", "trisno", "syahan",
             "raju", "heru", "nopiana", "wely", "laila"]

# Shift kerja per hari untuk setiap karyawan
shifts = {
    "mon": ["pg", "siang", "pg", "siang", "pg", "pg", "siang", "siang", "pg", "off"],
    "tue": ["siang", "pg", "pg", "off", "pg", "siang", "siang", "siang", "pg", "pg"],
    "wed": ["siang", "off", "pg", "pg", "siang", "off", "siang", "siang", "pg", "pg"],
    "thu": ["pg", "siang", "pg", "pg", "siang", "siang", "pg", "siang", "pg", "pg"],
    "fri": ["siang", "pg", "pg", "pg", "siang", "siang", "pg", "off", "off", "pg"],
    "sat": ["siang", "pg", "pg", "pg", "siang", "siang", "pg", "pg", "siang", "pg"],
    "sun": ["pg", "siang", "off", "pg", "siang", "siang", "pg", "pg", "siang", "pg"]
}

# Membuat edges jika ada shift yang sama di hari yang sama
for day in shifts:
    for i in range(len(employees)):
        for j in range(i+1, len(employees)):
            if shifts[day][i] != "off" and shifts[day][i] == shifts[day][j]:
                G.add_edge(employees[i], employees[j])

# Pewarnaan graf dengan algoritma greedy
color_map = nx.coloring.greedy_color(G, strategy="largest_first")

# Konversi warna menjadi daftar warna untuk plotting
colors = ["red", "blue", "green", "orange", "purple", "yellow"]
node_colors = [colors[color_map[node] % len(colors)] for node in G.nodes]

# Visualisasi graf
plt.figure(figsize=(12, 8))
nx.draw(G, with_labels=True, node_color=node_colors, node_size=2000, font_color="black")
plt.title("Pewarnaan Graf Berdasarkan Jadwal Shift Kerja")
plt.show()