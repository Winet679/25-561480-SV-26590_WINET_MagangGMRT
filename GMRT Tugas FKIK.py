import numpy as np

print("GMRT DAY 2: STUDI KASUS FK/IK")
print("Oleh: Winet P. Ginting (25/561480/SV/26590)")
print("-------------------------------------------")

print("Diketahui: \nteta 1 = 40º \nteta 2 = 30º \nfemur (l1) = 80 \ntibia (l2) = 90")
print("\nSilakan pilih salah satu")
print("1. Forward Kinematics")
print("2. Inverse Kinematics")
pil = int(input("Pilihan (1 atau 2): "))

t1, t2 = np.radians(40), np.radians(30)
t1+t2 == np.radians(40+30) 
l1, l2 = 80, 90

hasil = np.array([[np.cos(t1+t2), -np.sin(t1+t2), l1*np.cos(t1)+l2*np.cos(t1+t2)],
                  [np.sin(t1+t2), np.cos(t1+t2), l1*np.sin(t1)+l2*np.sin(t1+t2)],
                  [0, 0, 1]])

x, y = hasil[0][2], hasil[1][2]

teta2 = np.arccos((x**2 + y**2 - l1**2 - l2**2)/(2*l1*l2))
teta1 = np.arctan(y/x) - np.arctan((l2*np.sin(t2))/(l1+l2*np.cos(t2)))

if pil == 1:
    print("\nHomogenous Transform Matrix: \n", hasil)
    print("Koordinat titik akhir ujung kaki robot adalah (%.2f, %.2f)" %(x, y))
elif pil == 2:
    print("\nMelalui FK didapat titik akhir (%.2f, %.2f). Melalui IK diperoleh sudut putaran servo yang diperlukan untuk mencapai titik tersebut:" %(x, y))
    print("teta 1 = %.2f \nteta 2 = %.2f" %(np.degrees(teta1), np.degrees(teta2)))
else:
    print("Pilihan tidak valid.")