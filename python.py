
#Python Uygulama 2

#kütüphanenin tanımlanması:
import math
# 1. Points listesinin tanımlanması:
points = [(1, 2), (4, 6), (5, 8), (2, 1), (3, 4)]

# 2. Öklid mesafesi fonksiyonunu içeren kod:
def euclideanDistance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# 3. Mesafelerin hesaplanmasını gerçekleştiren kod: 
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

# 4. Minimum mesafenin bulunması işlemini gerçekleştiren kod:
min_distance = min(distances)

# Minimum mesafeyi yazdırma işlemini gerçekleştiren kod:
print("Minimum mesafe:", min_distance)
