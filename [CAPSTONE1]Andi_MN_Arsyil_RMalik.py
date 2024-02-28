from tabulate import tabulate
# Dictionary untuk Daftar Beras Beserta Detailnya
riceStore = {
    'A01':{'berasMerk':'Sukanassi', 'berasBerat':5, 'berasHarga':65000, 'berasTersedia':5, 'berasTerjual':400, 'berasModal':60000, 'stokTotal':400},
    'A02':{'berasMerk':'Sania', 'berasBerat':5, 'berasHarga':54000, 'berasTersedia':0, 'berasTerjual':400, 'berasModal':47500, 'stokTotal':400},
    'A03':{'berasMerk':'Raja', 'berasBerat':5, 'berasHarga':71000, 'berasTersedia':1, 'berasTerjual':500, 'berasModal':68000, 'stokTotal':500},
    'A04':{'berasMerk':'Maksyuss', 'berasBerat':5, 'berasHarga':51000, 'berasTersedia':0, 'berasTerjual':400, 'berasModal':49500, 'stokTotal':400},
    'A05':{'berasMerk':'Maksyuss', 'berasBerat':5, 'berasHarga':51000, 'berasTersedia':0, 'berasTerjual':400, 'berasModal':49500, 'stokTotal':400}
}
# Dictionary untuk Daftar Expenses pada Toko
storeExpenses = {
    'B01':{'namaExpenses':'Iklan', 'Biaya':50000},
    'B02':{'namaExpenses':'Pengiriman', 'Biaya':67000}
}
# Dictionary untuk Daftar Akun Karyawan Toko
accountEmployee = {
    '1':{'pass':'1'}
}

def loginEmployee():
    # Menampilkan Menu Login untuk Masuk Kedalam Program Toko
    while True:
        sureLogin = input('\nHello, BeBeras Employee!\n[1]Login for Employee\n[2]Exit\nEnter Your Choice : ')
        if sureLogin == '1': 
            print('\nEnter your account:')
            unameEmployee = input('Username : ')
            passEmployee = input('Password : ')
            if unameEmployee in accountEmployee and passEmployee == accountEmployee[unameEmployee]['pass']:
                menuEmployee()
            else:
                # Menampilkan Notification Account Salah
                print('\nYour username or password is wrong!')        
        elif sureLogin == '2':
            # Memberhentikan Program
            break
        else:
            # Menampilkan Notification Ketika Inputan Salah
            print('\nThe option you entered is not valid.')
def menuEmployee():
    while True:
        inputMenuEmployee = input('''
Welcome to Beberas Program for Employee! Choose the menu option:
[1] Information Data
[2] Add New Data
[3] Update and Edit Data
[4] Delete Data
[5] Exit from Beberas Program for Employee
Enter Your Choice : ''')
        if inputMenuEmployee == '1':
            # Fungsi Read Data
            infoEmployee()
        elif inputMenuEmployee == '2':
            # Fungsi Create Data
            addEmployee()
        elif inputMenuEmployee == '3':
            # Fungsi Update Data
            editUpdateEmployee()
        elif inputMenuEmployee == '4':
            # Fungsi Delete Data
            deleteEmployee()
        elif inputMenuEmployee == '5':
            # Keluar dari Akun Employee
            break
        else:
            # Menampilkan Notification Inputan Salah
            print('\nThe option you entered is not valid.')

def infoEmployee():
    while True:
        inputInfoEmployee = input('''
Data Information, You can see data details in this side, Enjoy!
[1] Items Information
[2] Finance Information
[3] Back to Main Menu
Enter Your Choice: ''')
        if inputInfoEmployee == '1':
            infoItems()
        elif inputInfoEmployee == '2':
            infoFinance()
        elif inputInfoEmployee == '3':
            break
        else:
            print('\nThe option you entered is not valid.')
def infoItems():
    while True:
        inputInfoCustomer = input('''
Rice Data. This side you can see about Rice Data, Enjoy!
[1] All Rice Data
[2] Rice on Stock
[3] Filter Rice Data
[4] Best Seller
[5] Back to Main Menu
Enter Your Choice: ''')
        if inputInfoCustomer == '1':
            riceAll()
        elif inputInfoCustomer == '2':
            riceOnStock()
        elif inputInfoCustomer == '3':
            riceFilter()
        elif inputInfoCustomer == '4':
            riceBestSeller()
        elif inputInfoCustomer == '5':
            break
        else:
            print('\nThe option you entered is not valid.')
def riceAll():
    listAwal=[]
    for key, value in riceStore.items():
        id = key
        listBaru = [id, value['berasMerk'],value['berasBerat'],value['berasHarga'],value['berasTersedia']]
        listAwal.append(listBaru)
    print(tabulate(listAwal, headers=['Code', 'Rice Mek', 'Weight', 'Price of Rice', 'Rice on Stock'], tablefmt='fancy_grid'))
    if len(riceStore) == 0:
        print("\t\tData Doens't Exists")
def riceOnStock():
    listAwal=[]
    for key, value in riceStore.items():
        if riceStore[key]['berasTersedia'] > 0:
            id = key
            listBaru = [id, value['berasMerk'],value['berasBerat'],value['berasHarga'],value['berasTersedia']]
            listAwal.append(listBaru)
    print(tabulate(listAwal, headers=['Code', 'Rice Mek', 'Weight', 'Price of Rice', 'Rice on Stock'], tablefmt='fancy_grid'))
    if len(listAwal) == 0:
        print("\t\tRice Stock Runs Out")
def riceFilter():
    inputFilter = input('Enter code of rice to see the data : ')
    listAwal=[]
    for key, value in riceStore.items():
        id=key
        listBaru = [id, value['berasMerk'],value['berasBerat'],value['berasHarga'],value['berasTersedia']]
        if inputFilter.upper() == id:
            listAwal.append(listBaru)
    if len(listAwal) == 1:
        print(tabulate(listAwal, headers=['Code', 'Rice Mek', 'Weight', 'Price of Rice', 'Rice on Stock'], tablefmt='fancy_grid'))
    else:
        print("\nThe code doesn't exists")
def riceBestSeller():
    riceBest = dict(sorted(riceStore.items(), key=lambda x:x[1]['berasTerjual'],reverse=True))
    listAwal = []
    for key, value in riceBest.items():
        id = key
        listBaru = [id, value['berasMerk'],value['berasBerat'],value['berasHarga'], value['berasTerjual']]
        listAwal.append(listBaru)
    print(tabulate(listAwal, headers=['Code','Rice Merk', 'Weight', 'Price of Rice','Quantity Sold Rice'], tablefmt='fancy_grid'))
    if len(riceStore) == 0:
        print("\t\tData Doens't Exists")
def infoFinance():
    while True:
        print('\nFinance of BeBeras Information :\n[1] Expenses Details\n[2] Gross Profit Details\n[3] Income Statement')
        info = input('[4] Exit\nEnter Your Choice : ') 
        if info == '1':
            infoExpenses()
        elif info == '2':
            infoGrossProfit()
        elif info == '3':
            infoIncomeStatement()
        elif info == '4':
            break
def infoExpenses():
    listAwal=[]
    for key, value in storeExpenses.items():
        id = key
        listBaru = [id,value['namaExpenses'],value['Biaya']]
        listAwal.append(listBaru)
    print(tabulate(listAwal, headers=['Code','Expenses Name', 'Expenses Cost'], tablefmt='fancy_grid'))
    if len(storeExpenses) == 0:
        print("\t\tData Doens't Exists")
def infoGrossProfit():
    while True:
        info = input('\nEnter Your Page:\n[1]First Page\n[2]Second Page\n[3]Exit\nEnter your choice: ')
        if info == '1':
            infoGP1()
        elif info == '2':
            infoGP2()
        elif info == '3':
            break
        else:
            print('\nThe option you entered is not valid.')
def infoGP1():
    listAwal=[]
    for key, value in riceStore.items():
        id = key
        listBaru = [value['berasMerk'],value['berasHarga'], value['berasTerjual'], value['berasHarga']*value['berasTerjual']]
        listAwal.append(listBaru)
    print(tabulate(listAwal, headers=['Rice Merk', 'Price of Rice', 'Quantity Sold Rice', 'Total Sold Rice(Rp)'], tablefmt='fancy_grid'))
    if len(riceStore) == 0:
        print("\t\tData Doens't Exists")
def infoGP2():
    listAwal=[]
    for key, value in riceStore.items():
        id = key
        listBaru = [value['berasMerk'],value['berasModal'],value['stokTotal'], value['berasModal']*value['stokTotal'], (value['berasHarga']*value['berasTerjual'])-(value['berasModal']*value['stokTotal'])]
        listAwal.append(listBaru)
    print(tabulate(listAwal, headers=['Rice Merk','Purchase of Rice', 'Quantity First Stock', 'Total Purchase of Rice (Rp) ', 'Gross Profit'], tablefmt='fancy_grid'))
    if len(riceStore) == 0:
        print("\t\tData Doens't Exists")
def infoIncomeStatement():
    sales = 0
    purchase = 0
    totalExpenses = 0
    for i in riceStore:
        sales = sales + (riceStore[i]['berasHarga'])*(riceStore[i]['berasTerjual'])
        purchase = purchase + (riceStore[i]['berasModal'])*(riceStore[i]['stokTotal'])
    labaKotor = sales - purchase
    for e in storeExpenses:
        totalExpenses = totalExpenses + (storeExpenses[e]['Biaya'])
    netIncome =  labaKotor - totalExpenses
    print(f'\nIncome Statement BeBeras Store!:\nTotal Sales          : {sales}')
    print(f'Total Purchase       : {purchase}\nGross Profit         : {labaKotor}')
    print(f'Total Expenses Cost  : {totalExpenses}\nProfit or Defisit    : {netIncome}')

def addEmployee():
    while True:
        inputaddEmployee = input('''
Add new data. This side you can create new data one or more directly, Enjoy!
[1] Add New Rice (One Data)
[2] Add New Rice (Many Data)
[3] Add New Expenses
[4] Back to Main Menu
Enter Your Choice: ''')
        if inputaddEmployee == '1':
            # Fungsi Buat Satu Data Baru
            addOne()
        elif inputaddEmployee == '2':
            # Fungsi Buat Satu atau Lebih Data Baru
            addMany()
        elif inputaddEmployee == '3':
            # Fungsi Buat Satu Data Baru
            addExpenses()
        elif inputaddEmployee == '4':
            # Kembali ke Menu Utama
            break
        # Menampilkan Notification Ketika Inputan Salah
        else:
            print('\nThe option you entered is not valid.')
def addOne():
    # Pada Penambahan Satu Data Beras, Tidak Akan Keluar Dari Program Hingga Inputannya Benar Sesuai Syarat
    while True:
        # Kode Beras Hanya Bisa Alfabet dan Angka, Serta Harus Berisikan 3 Karakter
        print('\n!!The code free alpha and digit but must 3 characters!!')
        baruRiceData = input('Enter new code: ').upper()
        # Mengecek Inputan Kode Sudah Ada atau Tidak
        if baruRiceData in riceStore:
            print('\nThe code already exists!')
            continue
        else:
            # Mengecek Inputan Sesuai Syarat atau Tidak
            if baruRiceData.isalnum() and len(baruRiceData) == 3:
                print("\nCreate Rice Data: ")
                riceBaru = input('\nRice Merk: ')
                break
            # Akan Meminta Input Hingga Inputan Benar
            else:
                print('\nPlease Enter Again!')
    while True:
        weightBaru = input('Weight of Rice(Kg): ')
        # Mengecek Inputan Berat Beras Digit atau Bukan
        if weightBaru.isdigit():
            break
        # Akan Meminta Input Hingga Inputan Benar
        else:
            print('\nPlease Enter Again!')
    while True:
        priceBaru = input('New Price of Rice: ')
        # Mengecek Inputan Harga Beras Digit atau Bukan
        if priceBaru.isdigit():
            break
        # Akan Meminta Input Hingga Inputan Benar
        else:
            print('\nPlease Enter Again!')
    while True:
        purchaseBaru = input('Purchase of Rice: ')
        # Mengecek Inputan Modal Beras Digit atau Bukan
        if purchaseBaru.isdigit():
            break
        # Akan Meminta Input Hingga Inputan Benar
        else:
            print('\nPlease Enter Again!')
    while True:
        stockBaru = input('Stock of Rice: ')
        # Mengecek Inputan Stok Beras Digit atau Bukan
        if stockBaru.isdigit():
            break
        # Akan Meminta Input Hingga Inputan Benar
        else:
            print('\nPlease Enter Again!')
    while True:        
        a,b,c,d = int(weightBaru),int(priceBaru),int(purchaseBaru),int(stockBaru)
        # Membuat Kondisi Nilai Tidak Boleh Dibawah 0
        if a >= 0 and b >= 0 and c >= 0 and d >= 0:
            yakin = input('Are you sure to create new rice data (Y/N): ')
            # Data Berhasil Terbuat dan Keluar dari Fungsi Ini
            if yakin.upper() == 'Y':
                i = baruRiceData.upper()
                riceStore[i] = {}
                riceStore[i]['berasMerk'] = riceBaru.capitalize()
                riceStore[i]['berasBerat'] = a
                riceStore[i]['berasHarga'] = b
                riceStore[i]['berasModal'] = c
                riceStore[i]['berasTerjual'] = 0
                riceStore[i]['berasTersedia'] = d
                riceStore[i]['stockTotal'] = d
                print('\nYour new rice data successfully added!')
                break
            # Data Tidak Berhasil Terbuat dan Keluar dari Fungsi Ini
            elif yakin.upper() == 'N':
                print('\nYour new rice data unsuccessfully added!')
                break
            # Akan Meminta Input Hingga Inputan Benar
            else:
                print('Please Enter Again')
        # Akan Meminta Input Hingga Inputan Benar
        else:
            print('Please Enter Again')
def addMany():
    # Pada Penmabahan Satu atau Lebih Data, Ketika Inputan Salah atau Tidak Sesuai, 
    # Maka Inputan Tersebut Tidak akan Meminta Inputan Hingga Benar atau Sesuai Syarat.
    quantityrice = input('\nEnter Quanity New Data Do you Want to Create: ')
    if quantityrice.isdigit():
        # Melakukan Looping sesuai dengan Angka Inputan
        for j in range(int(quantityrice)):
            print('\n!!The code free alpha and digit but must 3 characters!!')
            i = input(f'Enter new code {j+1}: ')
            if i.upper() in riceStore:
                print('\nThe code already exists!')
            else:
                # Mengecek Inputan Sesuai Syarat atau Tidak
                if i.isalnum() and len(i) == 3:
                    print(f"\nCreate Rice Data {j+1}: ")
                    riceBaru = input('\nRice Merk: ')
                    weightBaru = input('Weight of Rice(Kg): ')
                    # Mengecek Inputan Berat Beras Digit atau Bukan
                    if weightBaru.isdigit():
                        priceBaru = input('New Price of Rice: ')
                        # Mengecek Inputan Harga Beras Digit atau Bukan
                        if priceBaru.isdigit():
                            purchaseBaru = input('Purchase of Rice: ')
                            # Mengecek Inputan Modal Beras Digit atau Bukan
                            if purchaseBaru.isdigit():
                                stockBaru = input('Stock of Rice: ')
                                # Mengecek Inputan Stok Beras Digit atau Bukan
                                if stockBaru.isdigit():
                                    a,b,c,d = int(weightBaru),int(priceBaru),int(purchaseBaru),int(stockBaru)
                                    # Membuat Kondisi Nilai Tidak Boleh Dibawah 0
                                    if a >= 0 and b >= 0 and c >= 0 and d >= 0:
                                        yakin = input('Are you sure to create new rice data (Y/N): ')
                                        # Data Berhasil Terbuat
                                        if yakin.upper() == 'Y':
                                            riceStore[i.upper()] = {}
                                            riceStore[i.upper()]['berasMerk'] = riceBaru.capitalize()
                                            riceStore[i.upper()]['berasBerat'] = a
                                            riceStore[i.upper()]['berasHarga'] = b
                                            riceStore[i.upper()]['berasModal'] = c
                                            riceStore[i.upper()]['berasTerjual'] = 0
                                            riceStore[i.upper()]['berasTersedia'] = d
                                            riceStore[i.upper()]['stockTotal'] = d
                                            print('\nYour new rice data successfully added!')
                                        # Data Tidak Berhasil Terbuat
                                        else:
                                            print('\nYour new rice data unsuccessfully added!')
                                    # Menampilkan Notification Inputan Salah
                                    else:
                                        print('\nYour input is not valid')
                                # Menampilkan Notification Inputan Salah
                                else:
                                    print('\nYour stock input is not valid')
                            # Menampilkan Notification Inputan Salah
                            else:
                                print('\nYour purchase of rice input is not valid')
                        # Menampilkan Notification Inputan Salah
                        else:
                            print('\nYour new price of rice input is not valid')
                    # Menampilkan Notification Inputan Salah
                    else:
                        print('\nYour weight of rice input is not valid')
                # Menampilkan Notification Inputan Salah
                else:
                    print('\nThe code not eligible!')
    # Menampilkan Notification Inputan Salah
    else:
        print('\nThe enter is not valid!')
def addExpenses():
    # Kode Expenses Hanya Bisa Alfabet dan Angka, Serta Harus Berisikan 3 Karakter
    print('\n!!The code free alpha and digit but must 3 characters!!')
    baruExpenses = input('Enter new code: ').upper()
    # Mengecek Inputan Kode Sudah Ada atau Tidak
    if baruExpenses in storeExpenses:
        print('\nThe code already exists!')
    else:
        # Mengecek Inputan Sesuai Syarat atau Tidak
        if baruExpenses.isalnum() and len(baruExpenses) == 3:
            print("\nCreate Expenses Data: ")
            exBaru = input('\nEnter expenses name: ')
            biayaBaru = input('Enter expenses cost: ')
            # Mengecek Inputan Biaya Expenses Digit atau Bukan
            if biayaBaru.isdigit():
                while True:
                    yakin = input('Are you sure to create new expenses data (Y/N): ')
                    # Data Berhasil Terbuat dan Keluar dari Fungsi Ini
                    if yakin.upper() == 'Y':
                        i = baruExpenses.upper()
                        storeExpenses[i] = {}
                        storeExpenses[i]['namaExpenses'] = exBaru.capitalize()
                        storeExpenses[i]['Biaya'] = int(biayaBaru)
                        print('\nYour new expenses data successfully added!')
                        break
                    # Data Tidak Berhasil Terbuat dan Keluar dari Fungsi Ini
                    elif yakin.upper() == 'N':
                        print('\nYour new expenses data unsuccessfully added!')
                        break
                    # Akan Meminta Input Hingga Inputan Benar
                    else:
                        print('\nPlease Enter Again!')
            # Menampilkan Notification Inputan Salah
            else:
                print('\nThe cost not eligible!')
        # Menampilkan Notification Inputan Salah
        else:
            print('\nThe code not eligible!')

def editUpdateEmployee():
    while True:
        inputaddEmployee = input('''
Edit and update data. This side you can edit or update data one or more data directly, Enjoy!
[1] Edit Data
[2] Update Data
[3] Back to Main Menu
Enter Your Choice: ''')
        if inputaddEmployee == '1':
            # Fungsi Menu Edit
            editEmployee()
        elif inputaddEmployee == '2':
            # Fungsi Menu Update
            updateEmployee()
        elif inputaddEmployee == '3':
            # Kembali ke Menu Utama
            break
        else:
            print('\nThe option you entered is not valid.')
def editEmployee():
        while True:
            inputaddEmployee = input('''
Edit you data, Enjoy!
[1] Edit Rice Data(One Values)
[2] Edit Expenses Data
[3] Back to Main Menu
Enter Your Choice: ''')
            if inputaddEmployee == '1':
                # Fungsi Edit One Value
                editOneV()
            elif inputaddEmployee == '2':
                # Fungsi Edit Satu Data Expenses
                editExpenses()
            elif inputaddEmployee == '3':
                # Kembali ke Menu Edit and Update
                break
            # Menampilkan Notification Ketika Inputan Salah
            else:
                print('\nThe option you entered is not valid.')
def editOneV():
    inputOneV = input('\nEnter code do you want to edit: ')
    if inputOneV.upper() in riceStore:
        print('\nWhat the column do you want to edit?\n[1]Rice Merk\n[2]Weight of Rice\n[3]Price of Rice')
        inputan = input('[4]Purchase of Rice\nEnter Your Choice: ')
        if inputan =='1':
            inputan1 = input('\nEnter Rice Merk: ')
            while True:
                yakin = input('Are you sure to edit rice merk (Y/N): ')
                if yakin.upper() == 'Y':
                    riceStore[inputOneV.upper()]['berasMerk'] = inputan1.capitalize()
                    print('\nYour edit rice merk successfully updated!')
                    break
                elif yakin.upper() == 'N':
                    print('\nYour edit rice merk unsuccessfully updated!')
                    break
                else:
                    print('\nPlease Enter Again')
        elif inputan =='2':
            inputan2 = input('\nEnter Weight of Rice: ')
            if inputan2.isdigit():
                while True:
                    yakin = input('Are you sure to edit weight of rice (Y/N): ')
                    if yakin.upper() == 'Y':
                        riceStore[inputOneV.upper()]['berasBerat'] = int(inputan2)
                        print('\nYour edit weight of rice successfully updated!')
                        break
                    elif yakin.upper() == 'N':
                        print('\nYour edit weight of rice unsuccessfully updated!')
                        break
                    else:
                        print('\nPlease Enter Again')
            else:
                print('\nUnsuccessfully updated!')
        elif inputan =='3':
            inputan3 = input('\nEnter Price of Rice: ')
            if inputan3.isdigit():
                while True:
                    yakin = input('Are you sure to edit price of rice (Y/N): ')
                    if yakin.upper() == 'Y':
                        riceStore[inputOneV.upper()]['berasHarga'] = int(inputan3)
                        print('\nYour edit price of rice successfully updated!')
                        break
                    elif yakin.upper() == 'N':
                        print('\nYour edit price of rice unsuccessfully updated!')
                        break
                    else:
                        print('\nPlease Enter Again')
            else:
                print('\nUnsuccessfully updated!')
        elif inputan =='4':
            inputan4 = input('\nEnter Purchase of Rice: ')
            if inputan4.isdigit():
                while True:
                    yakin = input('Are you sure to edit purchase of rice (Y/N): ')
                    if yakin.upper() == 'Y':
                        riceStore[inputOneV.upper()]['berasModal'] = int(inputan4)
                        print('\nYour edit purchase of rice successfully updated!')
                        break
                    elif yakin.upper() == 'N':
                        print('\nYour edit purchase of rice unsuccessfully updated!')
                        break
                    else:
                        print('\nPlease Enter Again')
            else:
                print('\nUnsuccessfully updated!')
        else:
            print('\nThe option you entered is not valid.')
    else:
        print("\nThe Code doesn't exists")
def editExpenses(): 
    inputEditExpenses = input('\nEnter code of expenses: ')
    if inputEditExpenses.upper() in storeExpenses:
        print('\nWhat the column do you want to edit?\n[1]Expenses Name\n[2]Cost Expenses')
        inputan = input('Enter Your Choice : ')
        if inputan =='1':
            inputExpensesName = input('Enter New Expenses Name : ')
            while True:
                yakin = input('\nAre you sure to edit expenses name (Y/N): ')
                if yakin.upper() == 'Y':
                    storeExpenses[inputEditExpenses.upper()]['namaExpenses'] = inputExpensesName
                    print('\nYour edit expenses name successfully updated!')
                    break
                elif yakin.upper() == 'N':
                    print('\nYour edit expenses name unsuccessfully updated!')
                    break
                else:
                    print('\nPlease Enter Again')
        if inputan =='2':
            inputExpensesCost = input('\nEnter New Expenses Cost : ')
            if inputExpensesCost.isdigit():
                while True:
                    yakin = input('\nAre you sure to edit expenses Cost (Y/N): ')
                    if yakin.upper() == 'Y':
                        storeExpenses[inputEditExpenses.upper()]['Biaya'] = int(inputExpensesCost)
                        print('\nYour edit expenses Cost successfully updated!')
                        break
                    elif yakin.upper() == 'N':
                        print('\nYour edit expenses Cost unsuccessfully updated!')
                        break
                    else:
                        print('\nPlease Enter Again')
            else:
                print('\nPlease Enter Again')
        else:
            print('\nThe option you entered is not valid.')
    else:
        print("\nThe code of expenses doesn't exists")
def updateEmployee():
    while True:
        inputaddEmployee = input('''
[1] Update Rice Sold (One Data)
[2] Update Rice Sold (Many Data)
[3] Back to Main Menu
Enter Your Choice: ''')
        if inputaddEmployee == '1':
            # Fungsi Update Satu Data
            updateOne()
        elif inputaddEmployee == '2':
            # Fungsi Update Satu atau Lebih Data
            updateMany()
        elif inputaddEmployee == '3':
            # Kembali ke Menu Edit and Update
            break
        # Menampilkan Notification Ketika Inputan Salah
        else:
            print('\nThe option you entered is not valid.')
def updateOne():
    inputUpdateMany = input('\nEnter code rice data : ')
    if inputUpdateMany.upper() in riceStore:
        inputRiceSold = input('Enter the quantity of rice sold : ')
        if inputRiceSold.isdigit():
            a = riceStore[inputUpdateMany.upper()]['berasTerjual']
            b = riceStore[inputUpdateMany.upper()]['berasTersedia']
            a = a + (int(inputRiceSold))
            b = b - (int(inputRiceSold))
            if b >= 0:
                while True:
                    yakin = input('Are you sure to create new rice data (Y/N): ')
                    if yakin.upper() == 'Y':
                        riceStore[inputUpdateMany.upper()].update({'berasTersedia':b, 'berasTerjual':a})
                        print('\nYour update rice sold successfully updated!')
                        break
                    elif yakin.upper() == 'N':
                        print('\nYour update rice sold unsuccessfully updated!')
                        break
                    else:
                        print('Please Enter Again')
            else:
                print('\nYour update rice sold unsuccessfully updated!')
        else:
            print('\nYour input is not valid!')
    else:
        print("\nYour code doensn't exists")
def updateMany():
    quantityupdate = input('\nEnter Quantity Data Do you Want to Update: ')
    if quantityupdate.isdigit():
        for j in range(int(quantityupdate)):
            inputUpdateOne = input(f'\nEnter rice code {j+1}: ')
            if inputUpdateOne.upper() in riceStore:
                inputRiceSold = input('Enter the quantity of rice sold : ')
                if inputRiceSold.isdigit():
                    a = riceStore[inputUpdateOne.upper()]['berasTerjual']
                    b = riceStore[inputUpdateOne.upper()]['berasTersedia']
                    a = a + (int(inputRiceSold))
                    b = b - (int(inputRiceSold))
                    if b >= 0:
                        while True:
                            yakin = input('Are you sure to create new rice data (Y/N): ')
                            if yakin.upper() == 'Y':
                                riceStore[inputUpdateOne.upper()].update({'berasTersedia':b, 'berasTerjual':a})
                                print('\nYour update rice sold successfully updated!')
                                break
                            elif yakin.upper() == 'N':
                                print('\nYour update rice sold unsuccessfully updated!')
                                break
                            else:
                                print('Please Enter Again')
                    else:
                        print('\nYour update rice sold unsuccessfully updated!')
                else:
                    print('\nYour input is not valid!')
            else:
                print("\nThe code doesn't exists!")
    else:
        print("\nYour input is not valid!")

def deleteEmployee():
    while True:
        inputdeleteEmployee = input('''
[1] Delete Rice Data (One Data)
[2] Delete Rice data (Recent Data)
[3] Delete Rice Data (All Data)
[4] Delete Expenses Data 
[5] Back to Main Menu
Enter Your Choice: ''')
        if inputdeleteEmployee == '1':
            # Fungsi Hapus Satu Data Beras
            delOne()
        elif inputdeleteEmployee == '2':
            # Fungsi Hapus Item Terakhir dalam Dictionary
            delRecent()
        elif inputdeleteEmployee == '3':
            # Fungsi Hapus Semua Data Beras
            delAll()
        elif inputdeleteEmployee == '4':
            # Fungsi Hapus Satu Data Expenses
            delExpenses()
        elif inputdeleteEmployee == '5':
            # Kembali ke Menu Utama
            break
        else:
            print('\nThe option you entered is not valid.')
def delOne():
    riceDel = input('\nEnter Rice Code : ').upper()
    if riceDel in riceStore:
        while True:
            yakin = input('Are you sure to delete rice data (Y/N): ')
            # Data Berhasil Terhapus dan Keluar dari Fungsi Ini
            if yakin.upper() == 'Y':
                del riceStore[riceDel]
                print('\nYour rice data successfully deleted!')
                break
            # Data Tidak Berhasil Terhapus dan Keluar dari Fungsi Ini
            elif yakin.upper() == 'N':
                print('\nYour rice data unseccessfully deleted!')
                break
            # Akan Meminta Input Hingga Inputan Benar
            else:
                print('Enter Again!')
    # Menampilkan Notifikasi Ketika Kode Tidak Ada
    else:
        print("\nThe code doesn't exists!")
def delRecent():
    while True:
        yakin = input('\nAre you sure to delete recent rice data (Y/N): ')
        # Data Berhasil Terhapus dan Keluar dari Fungsi Ini
        if yakin.upper() == 'Y':
            riceStore.popitem()
            print('\nYour rice data successfully deleted!')
            break
        # Data Tidak Berhasil Terhapus dan Keluar dari Fungsi Ini
        elif yakin.upper() == 'N':
            print('\nYour rice data unseccessfully deleted!')
            break
        # Akan Meminta Input Hingga Inputan Benar
        else:
            print('Enter Again!')
def delAll():
    while True:
        yakin = input('\nAre you sure to delete all rice data (Y/N): ')
        # Data Berhasil Terhapus dan Keluar dari Fungsi Ini
        if yakin.upper() == 'Y':
            riceStore.clear()
            print('\nYour rice data successfully deleted!')
            break
        # Data Tidak Berhasil Terhapus dan Keluar dari Fungsi Ini
        elif yakin.upper() == 'N':
            print('\nYour rice data unseccessfully deleted!')
            break
        # Akan Meminta Input Hingga Inputan Benar
        else:
            print('Enter Again!')
def delExpenses():
    exDel = input('\nEnter Rice Code : ').upper()
    if exDel in storeExpenses:
        while True:
            yakin = input('Are you sure to delete rice data (Y/N): ')
            # Data Berhasil Terhapus dan Keluar dari Fungsi Ini
            if yakin.upper() == 'Y':
                del storeExpenses[exDel]
                print('\nYour rice data successfully deleted!')
                break
            # Data Tidak Berhasil Terhapus dan Keluar dari Fungsi Ini
            elif yakin.upper() == 'N':
                print('\nYour rice data unseccessfully deleted!')
                break
            # Akan Meminta Input Hingga Inputan Benar
            else:
                print('\nEnter Again!')
    # Menampilkan Notifikasi Ketika Kode Tidak Ada
    else:
        print("\nThe code doesn't exists!")

# Memanggil Fungsi untuk Menjalankan Program
loginEmployee()