import numpy as np

# Імпортуємо matplotlib для побудови 3D-графіків
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

lynx = np.array([
[209.70, 368.42], [157.63, 332.16], [118.82, 284.21], [80.95, 224.56], [43.08, 244.44], [20.36, 266.67], [-4.26, 293.57], [2.37, 263.16], [-20.36, 292.40], [-39.29, 299.42], [-21.30, 259.65],
[-50.65, 267.84], [-39.29, 242.11], [-55.38, 240.94], [-100.83, 300.58], [-149.11, 345.03], [-172.78, 361.40], [-189.82, 300.58], [-192.66, 225.73], [-181.30, 145.03], [-168.05, 104.09], [-184.14, 66.67],
[-186.98, 31.58], [-183.20, 3.51], [-208.76, -4.68], [-197.40, -29.24], [-182.25, -44.44], [-203.08, -43.27], [-172.78, -92.40], [-131.12, -126.32], [-101.78, -147.37], [-74.32, -163.74], [-110.30, -224.56],
[-143.43, -287.72], [-161.42, -240.94], [-282.60, -221.05], [-388.64, -205.85], [-370.65, -301.75], [-339.41, -397.66], [18.46, -397.66], [345.09, -400.00], [359.29, -378.95], [367.81, -342.69], [346.98, -
362.57], [363.08, -302.92], [357.40, -243.27], [348.88, -266.67], [336.57, -201.17], [290.18, -135.67], [240.00, -118.13], [258.93, -164.91], [257.99, -228.07], [252.31, -271.35], [256.09, -333.33],
[247.57, -359.06], [230.53, -307.60], [194.56, -238.60], [160.47, -181.29], [120.71, -149.71], [165.21, -132.16], [201.18, -100.58], [183.20, -99.42], [221.07, -73.68], [253.25, -24.56], [222.01, -23.39],
[251.36, -1.17], [262.72, 24.56], [234.32, 25.73], [214.44, 42.11], [202.13, 60.82], [220.12, 101.75], [234.32, 160.23], [240.00, 230.41], [232.43, 316.96]])


#transponation for multiplying in next step bc 71x2 xnat be * 2x2
lynxT = lynx.T
print (lynxT.shape)


def plot_shape(array, title):
    plt.figure(figsize=(6, 6))
    plt.fill(array[0],array[1])
    plt.axhline() #- додають осі.
    plt.axvline() #- додають осі.
    plt.axis("equal") # однаковий масштаб осей
    plt.title(title)
    plt.show()

# plot_shape(lynxT, "Original")
#
#
def stretch(array, a, b):
    copy_arr = array.copy()
    ##make matrixAB
    matrixA = np.array([[a,0],[0,b]])
    # stretching
    stretched = matrixA @ copy_arr #(a*x \ b*y)
    print(matrixA)
    plot_shape(stretched,"Stretch")
    return stretched

# # stretch(lynxT,1.5,0.7)
#
def shear(array, a, b):
    copy_arr = array.copy()
    ##make matrixAB
    matrixA = np.array([[1,a],[b,1]])
    # shearing
    sheared = matrixA @ copy_arr
    print(matrixA)
    plot_shape(sheared ,"Shear")
    return sheared

# # shear(lynxT, 0, 0)
# # shear(lynxT, 0.5, 0)
# # shear(lynxT, 0, 0.5)
#
#
def reflection(array, a, b):
    if a == 0 & b == 0:
        print("this values are not expected")
        return 0

    copy_arr = array.copy()
    ##make matrixAB
    matrix = np.array([[(a**2-b**2) , 2*a*b], [2*a*b, (b**2-a**2)]])
    matrixA = (1/(a**2 + b**2)) * matrix

    reflected = matrixA @ copy_arr
    print(matrixA)
    plot_shape(reflected, "Reflection")
    return reflected

# # reflection(lynxT, 1, 1)
# # reflection(lynxT, 1, 0)
# # reflection(lynxT, 0, 0)
# #
#
def rotation(array, theta_gradus):
    copy_arr = array.copy()
    ##make matrixAB
    theta = np.radians(theta_gradus)
    matrixA = np.array([[np.cos(theta), -1*np.sin(theta)], [np.sin(theta), np.cos(theta)]])
    rotated = matrixA @ copy_arr
    print(matrixA)
    plot_shape(rotated, f"Rotation {theta_gradus}")
    return rotated
# #
# # rotation(lynxT, 0)
# # rotation(lynxT, 90)
# # rotation(lynxT, 45)
#
#
# print("scenario 1")
# print("rotation 45 -> stretch 2 0.3 -> shear 0.2 0.7 -> reflection 1 0")
#
# S1 = reflection(shear(stretch(rotation(lynxT, 45),2,0.3),0.2,0.7),1,0)
#
# print("scenario 2")
# print("stretch 2 0.3 -> reflection 1 0 -> rotation 45 ->  shear 0.2 0.7 ")
#
# S2 = shear(rotation(reflection(stretch(lynxT,2,0.3),1,0),45), 0.2 , 0.7)
#
# print("scenario 3")
# print("reflection 1 0 -> rotation 45 ->   shear 0.2 0.7 -> stretch 2 0.3  ")
#
# S3 = stretch(shear(rotation(reflection(lynxT,1,0),45), 0.2, 0.7), 2, 0.3)
#
# if np.allclose(S1, S2) and np.allclose(S2, S3):
#     print("same")
# else:
#     print("s1 s2 s3 are different. result depend on the order")
#
# # 3D space

#from pdf
def read_off(filename: str):
    with open(filename, "r") as f:
        # Перевіряємо, чи перший рядок починається з OFF
        if "OFF" != f.readline().strip():
            raise ValueError("Not a valid OFF header")

        # Зчитуємо кількість вершин, граней та ребер (третє значення часто ігнорується)
        n_verts, n_faces, _ = map(int, f.readline().strip().split())

        # Зчитуємо координати всіх вершин (x, y, z)
        verts = [
            list(map(float, f.readline().strip().split()))
            for _ in range(n_verts)
        ]

        # Зчитуємо грані: перше число у рядку - кількість вершин грані (ігноруємо), далі індекси
        faces = [
            list(map(int, f.readline().strip().split()[1:]))
            for _ in range(n_faces)
        ]

        # Повертаємо вершини у вигляді масиву NumPy та список граней
        return np.array(verts), faces

# File reading
vertices, faces = read_off(
    "airplane/test/airplane_0628.off"
)
# print(vertices.shape)
# print(faces[:3])
# print(vertices)

def plot_off(vertices, faces, title):
    fig = plt.figure(figsize=(8, 8))  # створюємо вікно
    ax = fig.add_subplot(111, projection="3d")  # додаємо 3D координатну систему

    # Створюємо полігональну сітку з граней (faces) та додаємо її на графік
    mesh = Poly3DCollection(
        [vertices[face] for face in faces],
        alpha=0.3,
        edgecolor="k",  # прозорість 0.3, чорні ребра
    )
    ax.add_collection3d(mesh)

    # Додаємо вершини як червоні точки
    # ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], s=2, c="r")

    # Підписуємо осі
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    # Автоматично масштабуємо сцену під модель
    ax.auto_scale_xyz(vertices[:, 0], vertices[:, 1], vertices[:, 2])

    #not nessesary fom ai for better view
    ax.set_box_aspect(np.ptp(vertices, axis=0))
    #

    ax.set_title(title)

    plt.show()  # показуємо результат

# Виклик функції для побудови OFF-моделі
# plot_off(vertices, faces)



vertices_3D = vertices.T

def rotate_xy(array, theta):
    copy_arr = array.copy()
    theta_rad = np.radians(theta)
    matrixA = np.array([[np.cos(theta_rad), -1 * np.sin(theta_rad), 0], [np.sin(theta_rad), np.cos(theta_rad), 0],[0,0,1]])
    rotated = matrixA @ copy_arr
    print(matrixA)
    plot_off(rotated.T, faces,f"Rotation XY {theta}")
    return rotated

# rotate_xy(vertices_3D, 45)

def rotate_yz(array, theta):
    copy_arr = array.copy()
    theta_rad = np.radians(theta)
    matrixA = np.array([[1, 0, 0],[0,np.cos(theta_rad),-1 * np.sin(theta_rad)],[0,np.sin(theta_rad), np.cos(theta_rad)]])
    rotated = matrixA @ copy_arr
    print(matrixA)
    plot_off(rotated.T, faces, f"Rotation YZ {theta}")
    return rotated

# rotate_yz(vertices_3D, 45)

def rotate_xz(array, theta):
    copy_arr = array.copy()
    theta_rad = np.radians(theta)
    matrixA = np.array([[np.cos(theta_rad),0,-1 * np.sin(theta_rad)],[0,1,0],[np.sin(theta_rad), 0 ,np.cos(theta_rad)]])
    rotated = matrixA @ copy_arr
    print(matrixA)
    plot_off(rotated.T, faces, f"Rotation XZ {theta}")
    return rotated

# rotate_xz(vertices_3D, 45)

print("scenario 1")
print("rotation xy 30 -> rotation yz 45 -> rotation xz 20")

D1 = rotate_xz(rotate_yz(rotate_xy(vertices_3D, 30), 45),20)
print("scenario 2")
print("rotation yz 45 -> rotation xy 30 ->  rotation xz 20")

D2 =rotate_xz(rotate_xy(rotate_yz(vertices_3D, 45), 30),20)
print("scenario 3")
print(" rotation xz 20 -> rotation yz 45 -> rotation xy 30 ")
D3 = rotate_xy(rotate_yz(rotate_xy(vertices_3D, 20), 45),30)

if np.allclose(D1, D2) and np.allclose(D2, D3):
    print("same")
else:
    print("d1 d2 d3 are different. result depend on the order")
