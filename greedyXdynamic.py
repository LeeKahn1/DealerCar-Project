import time

#Header Kelompok
def headerKelompok(group_name, group_members):
    header = f"||Kelompok: {group_name}\n||Anggota:                          ||{', '.join(group_members)}"
    return header
print("======================================")
group_name = "Kelompok 8              ||"
group_members = ["\n" "||Angly Khan Surya - 1301213283     ||\n" "||Hadid Pilar Gautama - 1301213297  ||\n" "||Yuridikta Adha Muslim - 1301213054||"]
header = headerKelompok(group_name, group_members)
print(header)
print("======================================")

#membuat fungsi menu
def menu():
    print("======================================")
    print("    /\/\/\/\/\/\ MENU /\/\/\/\/\/\    ")
    print("======================================")
    print("0. Units")
    print("1. Knapsack Greedy")
    print("2. Knapsack Dynamic Programming")
    print("3. Kompleksitas")
    print("4. Keluar")


#Greedy
def knapsack_greedy(units, capacity):
    # Mengurutkan unit berdasarkan rasio profit/kapasitas secara menurun
    sorting_units = sorted(units, key=lambda x: x['profit'] / x['capacity'], reverse=True)

    total_profit = 0
    selected_units = []

    # Iterasi melalui daftar mobil yang sudah diurutkan
    for unit in sorting_units:
        # Jika kapasitas unit masih cukup, tambahkan unit ke dalam knapsack/garasi
        if unit['capacity'] <= capacity:
            # Tandai mobil tersebut sebagai mobil yang dibeli
            selected_units.append(unit)
            # Tambahkan profit mobil ke total_profit
            total_profit += unit['profit']
            # Kurangi garasi_capacity dengan kapasitas mobil
            capacity -= unit['capacity']

    return total_profit, selected_units

#Dynamic Programming
def knapsack_dynamicP(units, capacity):
    n = len(units)
    # Membuat matriks untuk menyimpan// hasil submasalah
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            # Jika kapasitas unit lebih kecil atau sama dengan kapasitas yang tersedia
            if units[i - 1]['capacity'] <= j:
                # Membandingkan nilai jika item tersebut diambil atau tidak diambil
                dp[i][j] = max(units[i - 1]['profit'] + dp[i - 1][j - units[i - 1]['capacity']], dp[i - 1][j])
            else:
                # Unit tidak dapat diambil karena kapasitas tidak mencukupi
                dp[i][j] = dp[i - 1][j]

    # Mencari item-item yang dipilih berdasarkan nilai dp terakhir
    selected_units = []
    i = n
    j = capacity
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            selected_units.append(units[i - 1])
            j -= units[i - 1]['capacity']
        i -= 1
    total_profit = dp[n][capacity]
    return total_profit, selected_units

# Daftar mobil dengan profit dan kapasitas
# Kode ini mendefinisikan daftar yang disebut unit yang berisi list.-
#-Setiap list mewakili satu mobil dan berisi informasi tentang pembuatan, model, keuntungan,-
#-dan kapasitas mobil. List di-assign ke variabel
units = [
    {'mobil': '(1)Audi', 'profit': 400, 'capacity': 1},
    {'mobil': '(2)Bentley', 'profit': 700, 'capacity': 2},
    {'mobil': '(3)Cadillac', 'profit': 600, 'capacity': 2},
    {'mobil': '(4)Daihatsu', 'profit': 200, 'capacity': 1},
    {'mobil': '(5)Esemka', 'profit': 100, 'capacity': 1},
    {'mobil': '(6)Ferrari', 'profit': 600, 'capacity': 1},
    {'mobil': '(7)GEA', 'profit': 300, 'capacity': 2},
    {'mobil': '(8)Hyundai', 'profit': 800, 'capacity': 2}
]

#Membuat visual blok garasi (greedy)
def draw_garage_greedy(blocks):
    for i in range(blocks):
        print("[ Audi ][Ferrari]")
        print("[ Hyun-][ -dai  ]")
        print("[ Bent-][ -ley  ]")
        print("[ Cadi-][ -llac ]")
    print()

#Membuat visual blok garasi (dynamic)
def draw_garage_dynamic(blocks):
    for i in range(blocks):
        print("[ Hyun- ][ -dai   ]")
        print("[Ferrari][  Audi  ]")
        print("[ Cadi- ][ -llac  ]")
        print("[ Bent- ][ -ley   ]")
    print()


while True:     #selama true, perulangan akan terus berjalan hingga terjadi break
    menu()      #menampilkan menu pada perulangan while
    pilih_input = input("Silahkan Pilih: ")
    if pilih_input == "0" :     #jika meilih 0, maka akan menampilkan unit yang akan dimasukkan ke garasi
        print("\nBerikut mobil yang tersedia: ")
        for unit in units :
            print(unit)

    if pilih_input == "1" :     #jika memilih 1, maka akan menampilkan strategi greedy
        # kapasitas garasi
        garage_capacity = 8

        # Memulai waktu eksekusi pada greedy
        start_time = time.time()    
        # Memanggil fungsi knapsack_greedy
        total_profit, selected_units = knapsack_greedy(units, garage_capacity)
        # Menghentikan waktu eksekusi pada greedy
        end_time = time.time()
        # Menghitung waktu eksekusi
        execution_time = end_time - start_time

        print("\nMobil yang dipilih untuk memaksimalkan profit:")
        for unit in selected_units:     # Kode ini digunakan untuk mengulang semua unit dalam list "selected_units" dan mencetak nilai "mobil" untuk setiap unit.
            print(unit['mobil'], "- Profit:", unit['profit'], "- Kapasitas:", unit['capacity'])
        # Total profit yang didapatkan adalah 3100$
        print("Total profit yang didapatkan:", total_profit, "$")
        # Menampilkan waktu eksekusi greeedy
        print("Waktu eksekusi Knapsack Greedy:", execution_time, "detik")
        # Visual Blok Garasi Strategi Greedy
        print("Isi Blok Garasi: ")
        draw_garage_greedy(1)
        

    elif pilih_input == "2":    #jika memilih 2 maka akan menampilkan strategi dynamic programming
        # kapasitas garasi
        garage_capacity = 8

        # Memulai waktu eksekusi pada dynamic programming
        start_time = time.time()
        # Memanggil fungsi knapsack_dynamicP
        total_profit, selected_units = knapsack_dynamicP(units, garage_capacity)
        end_time = time.time()
        execution_time = end_time - start_time

        print("\nMobil yang dipilih untuk memaksimalkan profit:")
        for unit in selected_units:
            print(unit['mobil'], "- Profit:", unit['profit'], "- Kapasitas:", unit['capacity'])
        # Total profit yang didapatkan adalah 3100$
        print("Total profit yang didapatkan:", total_profit, "$")
        # Menampilkan waktu eksekusi dynamic programming
        print("Waktu eksekusi Knapsack Dynamic Programming:", execution_time, "detik")
        # Visual BLok Garasi Strategi Dynamic Programming
        print("Isi Blok Garasi: ")
        draw_garage_dynamic(1)
        
    elif pilih_input == "3":    #Jika memilih 3 maka akan menampilkan kompleksitas dari fungsi greedy dan dp
        print("Fungsi knapsack_greedy() memiliki kompleksitas waktu O(n log n), di mana n adalah jumlah unit. Ini disebabkan oleh pengurutan unit berdasarkan rasio profit/kapasitas.\n")
        print("Fungsi knapsack_dynamicP() memiliki kompleksitas waktu O(n * capacity), di mana n adalah jumlah unit dan capacity adalah kapasitas garasi. Ini disebabkan oleh iterasi melalui matriks DP.\n")

    elif pilih_input == "4":    #Jika memilih 4 maka program akan selesai
        print(" /\/\/\/\/\/\/\/\/\/\ ")
        print("<  Hatur Thank YOU!  >")
        print(" \/\/\/\/\/\/\/\/\/\/ ")
        break