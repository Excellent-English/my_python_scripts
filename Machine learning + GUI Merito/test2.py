import matplotlib.pyplot as plt

# Dane do wykresów
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 35]
labels = ['A', 'B', 'C', 'D', 'E']
sizes = [15, 30, 45, 10, 20]  # Upewnij się, że masz 5 wartości, aby pasowały do 5 etykiet

# Wykres liniowy
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.plot(x, y, marker='o', linestyle='-', color='b')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Wykres liniowy')

# Wykres słupkowy
plt.subplot(1, 3, 2)
plt.bar(labels, sizes, color='g')
plt.xlabel('Kategoria')
plt.ylabel('Wartość')
plt.title('Wykres słupkowy')

# Wykres kołowy
plt.subplot(1, 3, 3)
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Wykres kołowy')

# Wyświetlenie wykresów
plt.tight_layout()
plt.show()