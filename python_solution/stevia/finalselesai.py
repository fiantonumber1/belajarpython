from os import name
from tkinter import *
from tkinter import messagebox
import random
import time
from tkinter import filedialog

root = Tk()
root.title("Login")
root.geometry("925x500+160+120")
root.configure(bg="#D9D9D9")
root.resizable(False, False)


clicked = False
clickedcroissant = False
clickedwaffle = False
clickedlasagna = False
clickedburger = False
clickedomelets = False
clickedsamosa = False
clickedavocadotoast = False
clickedtomatosoup = False

clickedamericano = False
clickedlemontea = False
clickedmocha = False
clickedespresso = False
clickedvanillalatte = False
clickedairmineral = False
clickedfruitysmoothies = False
clickedcappuchinocoffe = False
clickedcmatchalatte = False

clickedapplepie = False
clickedfrenchfries = False
clickedchurros = False
clickedcheesecake = False
clickedicecream = False
clickeddonuts = False
clickedchococupcake = False
clickedsaladbuah = False
clickedpudding = False


def signin():
    Username = user.get()
    Password = code.get()

    if Username == "admin" and Password == "1234":
        screen = Tk()
        screen.geometry("1150x600+0+0") 
        screen.resizable(True, True)
        screen.title("Stelliva Coffee Shop")  #nama aplikasi

        topFrame = Frame(screen, bd=5, relief=RIDGE, bg="white")  #frame judul
        topFrame.pack(side=TOP)

        labelTitle = Label(
            topFrame,
            text="STELLIVA",
            font=("Castellar", 25, "bold"),
            fg="white",
            bg="#53B0FC",
            bd=10,
            width=15,
        )  # judul aplikasi
        labelTitle.grid(row=0, column=10)

        screen.config(bg="#D9D9D9")

        # VARIABLE
        # Menentukan variables
        var1 = IntVar()
        var2 = IntVar()
        var3 = IntVar()
        var4 = IntVar()
        var5 = IntVar()
        var6 = IntVar()
        var7 = IntVar()
        var8 = IntVar()
        var9 = IntVar()
        var10 = IntVar()
        var11 = IntVar()
        var12 = IntVar()
        var13 = IntVar()
        var14 = IntVar()
        var15 = IntVar()
        var16 = IntVar()
        var17 = IntVar()
        var18 = IntVar()
        var19 = IntVar()
        var20 = IntVar()
        var21 = IntVar()
        var22 = IntVar()
        var23 = IntVar()
        var24 = IntVar()
        var25 = IntVar()
        var26 = IntVar()
        var27 = IntVar()

        # variabel menu brunch
        e_sandwich = StringVar()
        e_croissant = StringVar()
        e_waffle = StringVar()
        e_lasagna = StringVar()
        e_burger = StringVar()
        e_omelets = StringVar()
        e_samosa = StringVar()
        e_avocadotoast = StringVar()
        e_tomatosoup = StringVar()

        # variabel menu minuman
        e_americano = StringVar()
        e_lemontea = StringVar()
        e_mocha = StringVar()
        e_espresso = StringVar()
        e_vanillalatte = StringVar()
        e_airmineral = StringVar()
        e_fruitysmoothies = StringVar()
        e_cappuchinocoffe = StringVar()
        e_matchalatte = StringVar()

        # variabel menu dessert
        e_applepie = StringVar()
        e_frenchfries = StringVar()
        e_churros = StringVar()
        e_cheesecake = StringVar()
        e_icecream = StringVar()
        e_donuts = StringVar()
        e_chococupcake = StringVar()
        e_saladbuah = StringVar()
        e_pudding = StringVar()

        # variabel Harga dalam struk
        hargadaribrunchvar = StringVar()
        hargadariminumanvar = StringVar()
        hargadaridessertvar = StringVar()
        subtotalvar = StringVar()
        servicetaxvar = StringVar()
        totalcostvar = StringVar()
        taxvaluevar = StringVar()

        e_sandwich.set("0")
        e_croissant.set("0")
        e_waffle.set("0")
        e_lasagna.set("0")
        e_burger.set("0")
        e_omelets.set("0")
        e_samosa.set("0")
        e_avocadotoast.set("0")
        e_tomatosoup.set("0")

        e_americano.set("0")
        e_lemontea.set("0")
        e_mocha.set("0")
        e_espresso.set("0")
        e_vanillalatte.set("0")
        e_airmineral.set("0")
        e_fruitysmoothies.set("0")
        e_cappuchinocoffe.set("0")
        e_matchalatte.set("0")

        e_applepie.set("0")
        e_frenchfries.set("0")
        e_churros.set("0")
        e_cheesecake.set("0")
        e_icecream.set("0")
        e_donuts.set("0")
        e_chococupcake.set("0")
        e_saladbuah.set("0")
        e_pudding.set("0")

        # FUNGSI
        # Awal fungsi perhitungan harga total
        tax = 11 / 100

        def totalcost():
            # mengglobalkan beberapa variable terlebih dahulu
            global hargadaribrunch, hargadariminuman, hargadaridessert, subtotalItems, totaltax
            if (
                var1.get() != 0
                or var2.get() != 0
                or var3.get() != 0
                or var4.get() != 0
                or var5.get() != 0
                or var6.get() != 0
                or var7.get() != 0
                or var8.get() != 0
                or var9.get() != 0
                or var10.get() != 0
                or var11.get() != 0
                or var12.get() != 0
                or var13.get() != 0
                or var14.get() != 0
                or var15.get() != 0
                or var16.get() != 0
                or var17.get() != 0
                or var18.get() != 0
                or var19.get() != 0
                or var20.get() != 0
                or var21.get() != 0
                or var22.get() != 0
                or var23.get() != 0
                or var24.get() != 0
                or var25.get() != 0
                or var26.get() != 0
                or var27.get() != 0
                
            ):

                # Assuming these are the variables holding the values from Entry widgets
                item1_entry = textsandwich.get()
                item2_entry = textcroissant.get()
                item3_entry = textwaffle.get()
                item4_entry = textlasagna.get()
                item5_entry = textburger.get()
                item6_entry = textomelets.get()
                item7_entry = textsamosa.get()
                item8_entry = textavocadotoast.get()
                item9_entry = texttomatosoup.get()

            
                item1 = int(item1_entry) if item1_entry and item1_entry.strip() else 0
                item2 = int(item2_entry) if item2_entry and item2_entry.strip() else 0
                item3 = int(item3_entry) if item3_entry and item3_entry.strip() else 0
                item4 = int(item4_entry) if item4_entry and item4_entry.strip() else 0
                item5 = int(item5_entry) if item5_entry and item5_entry.strip() else 0
                item6 = int(item6_entry) if item6_entry and item6_entry.strip() else 0
                item7 = int(item7_entry) if item7_entry and item7_entry.strip() else 0
                item8 = int(item8_entry) if item8_entry and item8_entry.strip() else 0
                item9 = int(item9_entry) if item9_entry and item9_entry.strip() else 0

                
                item10 = (
                    int(textamericano.get())
                    if textamericano.get() and textamericano.get().strip()
                    else 0
                )
                item11 = (
                    int(textlemontea.get())
                    if textlemontea.get() and textlemontea.get().strip()
                    else 0
                )
                item12 = (
                    int(textmocha.get())
                    if textmocha.get() and textmocha.get().strip()
                    else 0
                )
                item13 = (
                    int(textespresso.get())
                    if textespresso.get() and textespresso.get().strip()
                    else 0
                )
                item14 = (
                    int(textvanillalatte.get())
                    if textvanillalatte.get() and textvanillalatte.get().strip()
                    else 0
                )
                item15 = (
                    int(textairmineral.get())
                    if textairmineral.get() and textairmineral.get().strip()
                    else 0
                )
                item16 = (
                    int(textfruitysmoothies.get())
                    if textfruitysmoothies.get() and textfruitysmoothies.get().strip()
                    else 0
                )
                item17 = (
                    int(textcappuchinocoffe.get())
                    if textcappuchinocoffe.get() and textcappuchinocoffe.get().strip()
                    else 0
                )
                item18 = (
                    int(textmatchalatte.get())
                    if textmatchalatte.get() and textmatchalatte.get().strip()
                    else 0
                )

                item19 = (
                    int(textapplepie.get())
                    if textapplepie.get() and textapplepie.get().strip()
                    else 0
                )
                item20 = (
                    int(textfrenchfries.get())
                    if textfrenchfries.get() and textfrenchfries.get().strip()
                    else 0
                )
                item21 = (
                    int(textchurros.get())
                    if textchurros.get() and textchurros.get().strip()
                    else 0
                )
                item22 = (
                    int(textcheesecake.get())
                    if textcheesecake.get() and textcheesecake.get().strip()
                    else 0
                )
                item23 = (
                    int(texticecream.get())
                    if texticecream.get() and texticecream.get().strip()
                    else 0
                )
                item24 = (
                    int(textdonuts.get())
                    if textdonuts.get() and textdonuts.get().strip()
                    else 0
                )
                item25 = (
                    int(textchococupcake.get())
                    if textchococupcake.get() and textchococupcake.get().strip()
                    else 0
                )
                item26 = (
                    int(textsaladbuah.get())
                    if textsaladbuah.get() and textsaladbuah.get().strip()
                    else 0
                )
                item27 = (
                    int(textpudding.get())
                    if textpudding.get() and textpudding.get().strip()
                    else 0
                )
               

                hargadaribrunch = (
                    (item1 * 28000)
                    + (item2 * 32000)
                    + (item3 * 29000)
                    + (item4 * 28000)
                    + (item5 * 31000)
                    + (item6 * 26000)
                    + (item7 * 38000)
                    + (item8 * 27000)
                    + (item9 * 29000)
                )
                hargadariminuman = (
                    (item10 * 20000)
                    + (item11 * 15000)
                    + (item12 * 15000)
                    + (item13 * 22000)
                    + (item14 * 18000)
                    + (item15 * 8000)
                    + (item16 * 22000)
                    + (item17 * 20000)
                    + (item18 * 15000)
                )
                hargadaridessert = (
                    (item19 * 18000)
                    + (item20 * 25000)
                    + (item21 * 25000)
                    + (item22 * 28000)
                    + (item23 * 16000)
                    + (item24 * 21000)
                    + (item25 * 23000)
                    + (item26 * 22000)
                    + (item27 * 15000)
                )

                

                subtotalItems = hargadaribrunch + hargadariminuman + hargadaridessert
                
                tax = 11 / 100
                
                totaltax = subtotalItems * tax

                total2 = subtotalItems+totaltax

                LabelHargadariBrunch.config(
                    text="Harga Brunch : " + str(hargadaribrunch)
                )
                LabelHargadariMinuman.config(
                    text="Harga Minuman : " + str(hargadariminuman)
                )
                LabelHargadariDessert.config(
                    text="Harga Dessert : " + str(hargadaridessert)
                )
                LabelSubTotal.config(text="Sub Total : " + str(subtotalItems))
                LabelTax.config(text="Service Tax : " + str(totaltax))
                total.config(text=f"Total: Rp {total2:.2f}")


        def hitung_kembalian():
            selected_method = dropdown.get()
            total2 = subtotalItems + totaltax
            try:
                bayarpel = float(bayar_entry.get())
            except ValueError:
                bayarpel = 0  # Atur bayarpel ke 0 jika terjadi kesalahan konversi

            
            kembalian = bayarpel - total2
            if selected_method in ["QRIS", "Transfer"]:
                kembalian2.config(text="Rp 0")
                total.config(text=f"Total: Rp {total2:.1f}")
            else:
                kembalian2.config(text=f"Rp {kembalian:.1f}")
                total.config(text=f"Total: Rp {total2:.1f}")
            
            #kasus khusus
            if bayarpel-total2<0:
                    kembalian2.config(text="Uang yang dibayar kurang")
            
            

        inputframe = Frame(screen, bd=10, relief=RIDGE, bg="#53B0FC") 
        inputframe.place(x=625, y=300) 

        total = Label (inputframe, text="Total :", font=("Arial Rounded MT", 12, "bold"))
        total.pack (padx=10, pady=10)
                 
        bayar = Label (inputframe, text="Bayar", font=("Calibri", 12), bg="#53B0FC")
        bayar.pack ()
        bayar = StringVar()
        bayar_entry = Entry(inputframe, textvariable=bayar)
        bayar_entry.pack(padx=10, pady=10, ipadx=40, expand=True)

        def show():
            selected_method = dropdown.get()
            metode_label.config(text=f"Metode yang dipilih: {selected_method}")
            if selected_method in ["QRIS", "Transfer"]:
                kembalian2.config(text="Rp 0")
                bayar_entry.delete(0, END)
                bayar_entry.config(state='readonly')  # Buat bayar_entry menjadi non-editable
            else:
                bayar_entry.config(state='normal')  # Buat bayar_entry editable lagi
        
        metode_list = ["Tunai", "QRIS", "Transfer"]
        dropdown = StringVar()
        dropdown.set(metode_list[0])  # Pilih tunai secara default
        
        # Dropdown menu untuk memilih metode pembayaran
        dropdown_menu = OptionMenu(inputframe, dropdown, *metode_list, command=lambda _: show())
        dropdown_menu.pack(padx=10, pady=10)

        buttonbayar = Button(inputframe, text="Pembayaran", command=show)
        buttonbayar.pack()

        # Label untuk menampilkan metode yang dipilih
        metode_label = Label(inputframe, text="")
        metode_label.pack(pady=10)

        button_hitung = Button(inputframe, text="Hitung Kembalian", command=hitung_kembalian)
        button_hitung.pack()

        kembalian2 = Label(inputframe, text="Rp 0")
        kembalian2.pack()



        





        inputframeadmin = Frame(screen, bd=10, relief=RIDGE, bg="#53B0FC") 
        inputframeadmin.place(x=10, y=80)

        admin = Label (inputframeadmin, text="Nama Admin", font=("Calibri", 16, "bold"), bg="#53B0FC", fg="black")
        admin.pack (side=LEFT)

        admin = StringVar()

        admin_entry = Entry(inputframeadmin, textvariable=admin)
        admin_entry.pack(padx=10, pady=10, ipadx=40, expand=True)


        # Batas fungsi perhitungan harga total

        # awal fungsi cetak struk
        def struk():
            global billnumber, date
            thsa = True
            if thsa:
                textStruk.delete(1.0, END)
                x = random.randint(100, 10000)
                billnumber = "BILL" + str(x)
                date = time.strftime("%d/%m/%Y")
                textStruk.insert(
                    END,
                    "Resep Ref:\t        " + billnumber + "\t         " + date + "\n",
                )
                nama_admin = (admin_entry.get())
                textStruk.insert(END, f"Cashier\t\t\t {nama_admin}\n\n")
                textStruk.insert(END, "**\n")
                textStruk.insert(END, "Items:\t\t          Harga Total (Rp)\n")
                textStruk.insert(END, "**\n")


                #Food
                if textsandwich.get() != "":
                    sandwich_qty = int(textsandwich.get()) if textsandwich.get().strip() else 0
                    sandwich_price = sandwich_qty * 28000
                    if sandwich_qty > 1:
                        textStruk.insert(
                            END,
                            f"sandwich x{sandwich_qty}\t\t\tRp. {sandwich_price}\n\n",
                        )
                    else:
                        textStruk.insert(
                            END,
                            f"sandwich\t\t\tRp. {sandwich_price}\n\n",
                        )

                if textcroissant.get() != "":
                    croissant_qty = int(textcroissant.get()) if textcroissant.get().strip() else 0
                    croissant_price = croissant_qty * 32000
                    if croissant_qty > 1:
                        textStruk.insert(
                            END,
                            f"croissant x{croissant_qty}\t\t\tRp. {croissant_price}\n\n",
                        )
                    else:
                        textStruk.insert(
                            END,
                            f"croissant\t\t\tRp. {croissant_price}\n\n",
                        )

                if textwaffle.get() != "":
                    waffle_qty = int(textwaffle.get()) if textwaffle.get().strip() else 0
                    waffle_price = waffle_qty * 29000
                    if waffle_qty > 1:
                        textStruk.insert(
                            END,
                            f"classic waffle x{waffle_qty}\t\t\tRp. {waffle_price}\n\n",
                        )
                    else:
                        textStruk.insert(
                            END,
                            f"classic waffle\t\t\tRp. {waffle_price}\n\n",
                        )

                if textlasagna.get() != "":
                    lasagna_qty = int(textlasagna.get()) if textlasagna.get().strip() else 0
                    lasagna_price = lasagna_qty * 28000
                    if lasagna_qty > 1:
                        textStruk.insert(
                            END,
                            f"lasagna x{lasagna_qty}\t\t\tRp. {lasagna_price}\n\n",
                        )
                    else:
                        textStruk.insert(
                            END,
                            f"lasagna\t\t\tRp. {lasagna_price}\n\n",
                        )

                if textburger.get() != "":
                    burger_qty = int(textburger.get()) if textburger.get().strip() else 0
                    burger_price = burger_qty * 31000
                    if burger_qty > 1:
                        textStruk.insert(
                            END,
                            f"burger x{burger_qty}\t\t\tRp. {burger_price}\n\n",
                        )
                    else:
                        textStruk.insert(
                            END,
                            f"burger\t\t\tRp. {burger_price}\n\n",
                        )

                if textomelets.get() != "":
                    omelets_qty = int(textomelets.get()) if textomelets.get().strip() else 0
                    omelets_price = omelets_qty * 26000
                    if omelets_qty > 1:
                        textStruk.insert(
                            END,
                            f"omelets x{omelets_qty}\t\t\tRp. {omelets_price}\n\n",
                        )
                    else:
                        textStruk.insert(
                            END,
                            f"omelets\t\t\tRp. {omelets_price}\n\n",
                        )

                if textsamosa.get() != "":
                    samosa_qty = int(textsamosa.get()) if textsamosa.get().strip() else 0
                    samosa_price = omelets_qty * 38000
                    if samosa_qty > 1:
                        textStruk.insert(
                            END,
                            f"samosa x{samosa_qty}\t\t\tRp. {samosa_price}\n\n",
                        )
                    else:
                        textStruk.insert(
                            END,
                            f"samosa\t\t\tRp. {samosa_price}\n\n",
                        )

                if textavocadotoast.get() != "":
                    avocadotoast_qty = int(textavocadotoast.get()) if textavocadotoast.get().strip() else 0
                    avocadotoast_price = avocadotoast_qty * 27000
                    if avocadotoast_qty > 1:
                        textStruk.insert(
                            END,
                            f"avocado toast x{avocadotoast_qty}\t\t\tRp. {avocadotoast_price}\n\n",
                        )
                    else:
                        textStruk.insert(
                            END,
                            f"avocado toast\t\t\tRp. {avocadotoast_price}\n\n",
                        )

                if texttomatosoup.get() != "":
                    tomatosoup_qty = int(texttomatosoup.get()) if texttomatosoup.get().strip() else 0
                    tomatosoup_price = tomatosoup_qty * 29000
                    if tomatosoup_qty > 1:
                        textStruk.insert(
                            END,
                            f"tomato soup x{tomatosoup_qty}\t\t\tRp. {tomatosoup_price}\n\n",
                        )
                    else:
                        textStruk.insert(
                            END,
                            f"tomato soup\t\t\tRp. {tomatosoup_price}\n\n",
                        )

                #Drink
                if textamericano.get() != "":
                    americano_qty = int(textamericano.get()) if textamericano.get().strip() else 0
                    americano_price = americano_qty * 20000
                    if americano_qty > 1:
                        textStruk.insert(
                            END,
                            f"americano x{americano_qty}\t\t\tRp. {americano_price}\n\n",
                        )
                    else:
                        textStruk.insert(
                            END,
                            f"americano\t\t\tRp. {americano_price}\n\n",
                        )

                if textlemontea.get() != "":
                    lemontea_qty = int(textlemontea.get()) if textlemontea.get().strip() else 0
                    lemontea_price = lemontea_qty * 15000
                    if lemontea_qty > 1:
                        textStruk.insert(
                            END,
                            f"lemon tea x{lemontea_qty}\t\t\tRp. {lemontea_price}\n\n",
                        )
                    else:
                        textStruk.insert(
                            END,
                            f"lemon tea\t\t\tRp. {lemontea_price}\n\n",
                        )

                if textmocha.get() != "":
                    mocha_qty = int(textmocha.get()) if textmocha.get().strip() else 0
                    mocha_price = mocha_qty * 15000
                    if mocha_qty > 1:
                        textStruk.insert(
                            END,
                            f"mocha x{mocha_qty}\t\t\tRp. {mocha_price}\n\n",
                        )
                    else:
                        textStruk.insert(
                            END,
                            f"mocha\t\t\tRp. {mocha_price}\n\n",
                        )

                if textespresso.get() != "":
                    espresso_qty = int(textespresso.get()) if textespresso.get().strip() else 0
                    espresso_price = espresso_qty * 22000
                    if espresso_qty > 1:
                        textStruk.insert(
                            END,
                            f"espresso x{espresso_qty}\t\t\tRp. {espresso_price}\n\n",
                        )
                    else:
                        textStruk.insert(
                            END,
                            f"espresso\t\t\tRp. {espresso_price}\n\n",
                        )

                if textvanillalatte.get() != "":
                    vanillalatte_qty = int(textvanillalatte.get()) if textvanillalatte.get().strip() else 0
                    vanillalatte_price = vanillalatte_qty * 18000
                    if vanillalatte_qty > 1:
                        textStruk.insert(
                            END,
                            f"vanilla latte x{vanillalatte_qty}\t\t\tRp. {vanillalatte_price}\n\n",
                        )
                    else:
                        textStruk.insert(
                            END,
                            f"vanillalatte\t\t\tRp. {vanillalatte_price}\n\n",
                        )

                if textairmineral.get() != "":
                    airmineral_qty = int(textairmineral.get()) if textairmineral.get().strip() else 0
                    airmineral_price = airmineral_qty * 8000
                    if airmineral_qty > 1:
                        textStruk.insert(
                            END,
                            f"air mineral x{airmineral_qty}\t\t\tRp. {airmineral_price}\n\n",
                        )
                    else:
                        textStruk.insert(
                            END,
                            f"air mineral\t\t\tRp. {airmineral_price}\n\n",
                        )

                if textfruitysmoothies.get() != "":
                    fruitysmoothies_qty = int(textfruitysmoothies.get()) if textfruitysmoothies.get().strip() else 0
                    fruitysmoothies_price = fruitysmoothies_qty * 22000
                    if fruitysmoothies_qty > 1:
                        textStruk.insert(
                            END,
                            f"smoothies x{fruitysmoothies_qty}\t\t\tRp. {fruitysmoothies_price}\n\n",
                        )
                    else:
                        textStruk.insert(
                            END,
                            f"smoothies\t\t\tRp. {fruitysmoothies_price}\n\n",
                        )

                if textcappuchinocoffe.get() != "":
                    cappuchinocoffe_qty = int(textcappuchinocoffe.get()) if textcappuchinocoffe.get().strip() else 0
                    cappuchinocoffe_price = cappuchinocoffe_qty * 20000
                    if cappuchinocoffe_qty > 1:
                        textStruk.insert(
                            END,
                            f"cappuchino coffee x{cappuchinocoffe_qty}\t\t\tRp. {cappuchinocoffe_price}\n\n",
                        )
                    else:
                        textStruk.insert(
                            END,
                            f"cappuchino coffee\t\t\tRp. {cappuchinocoffe_price}\n\n",
                        )

                if textmatchalatte.get() != "":
                    matchalatte_qty = int(textmatchalatte.get()) if textmatchalatte.get().strip() else 0
                    matchalatte_price = matchalatte_qty * 15000
                    if matchalatte_qty > 1:
                        textStruk.insert(
                            END,
                            f"matcha latte x{matchalatte_qty}\t\t\tRp. {matchalatte_price}\n\n",
                        )
                    else:
                        textStruk.insert(
                            END,
                            f"matcha latte\t\t\tRp. {matchalatte_price}\n\n",
                        )

                #Dessert
                if textapplepie.get() != "":
                    applepie_qty = int(textapplepie.get()) if textapplepie.get().strip() else 0
                    applepie_price = applepie_qty * 18000
                    if applepie_qty > 1:
                        textStruk.insert(
                            END,
                            f"apple pie x{applepie_qty}\t\t\tRp. {applepie_price}\n\n",
                        )
                    else:
                        textStruk.insert(
                            END,
                            f"apple pie\t\t\tRp. {applepie_price}\n\n",
                        )

                if textfrenchfries.get() != "":
                    frenchfries_qty = int(textfrenchfries.get()) if textfrenchfries.get().strip() else 0
                    frenchfries_price = frenchfries_qty * 25000
                    if frenchfries_qty > 1:
                        textStruk.insert(
                            END,
                            f"french fries x{frenchfries_qty}\t\t\tRp. {frenchfries_price}\n\n",
                        )
                    else:
                        textStruk.insert(
                            END,
                            f"french fries\t\t\tRp. {frenchfries_price}\n\n",
                        )

                if textchurros.get() != "":
                    churros_qty = int(textchurros.get()) if textchurros.get().strip() else 0
                    churros_price = churros_qty * 25000
                    if churros_qty > 1:
                        textStruk.insert(
                            END,
                            f"churros x{churros_qty}\t\t\tRp. {churros_price}\n\n",
                        )
                    else:
                        textStruk.insert(
                            END,
                            f"churros\t\t\tRp. {churros_price}\n\n",
                        )

                if textcheesecake.get() != "":
                    cheesecake_qty = int(textcheesecake.get()) if textcheesecake.get().strip() else 0
                    cheesecake_price = cheesecake_qty * 28000
                    if cheesecake_qty > 1:
                        textStruk.insert(
                            END,
                            f"cheese cake x{cheesecake_qty}\t\t\tRp. {cheesecake_price}\n\n",
                        )
                    else:
                        textStruk.insert(
                            END,
                            f"cheese cake\t\t\tRp. {cheesecake_price}\n\n",
                        )

                if texticecream.get() != "":
                    icecream_qty = int(texticecream.get()) if texticecream.get().strip() else 0
                    icecream_price = icecream_qty * 16000
                    if icecream_qty > 1:
                        textStruk.insert(
                            END,
                            f"ice cream x{icecream_qty}\t\t\tRp. {icecream_price}\n\n",
                        )
                    else:
                        textStruk.insert(
                            END,
                            f"ice cream\t\t\tRp. {icecream_price}\n\n",
                        )

                if textdonuts.get() != "":
                    donuts_qty = int(textdonuts.get()) if textdonuts.get().strip() else 0
                    donuts_price = donuts_qty * 21000
                    if donuts_qty > 1:
                        textStruk.insert(
                            END,
                            f"glazed donuts x{donuts_qty}\t\t\tRp. {donuts_price}\n\n",
                        )
                    else:
                        textStruk.insert(
                            END,
                            f"glazed donuts\t\t\tRp. {donuts_price}\n\n",
                        )

                if textchococupcake.get() != "":
                    chococupcake_qty = int(textchococupcake.get()) if textchococupcake.get().strip() else 0
                    chococupcake_price = chococupcake_qty * 23000
                    if chococupcake_qty > 1:
                        textStruk.insert(
                            END,
                            f"lemon cupcake x{chococupcake_qty}\t\t\tRp. {chococupcake_price}\n\n",
                        )
                    else:
                        textStruk.insert(
                            END,
                            f"lemon cupcake\t\t\tRp. {chococupcake_price}\n\n",
                        )

                if textsaladbuah.get() != "":
                    saladbuah_qty = int(textsaladbuah.get()) if textsaladbuah.get().strip() else 0
                    saladbuah_price = saladbuah_qty * 22000
                    if saladbuah_qty > 1:
                        textStruk.insert(
                            END,
                            f"salad buah x{saladbuah_qty}\t\t\tRp. {saladbuah_price}\n\n",
                        )
                    else:
                        textStruk.insert(
                            END,
                            f"salad buah\t\t\tRp. {saladbuah_price}\n\n",
                        )

                if textpudding.get() != "":
                    pudding_qty = int(textpudding.get()) if textpudding.get().strip() else 0
                    pudding_price = pudding_qty * 15000
                    if pudding_qty > 1:
                        textStruk.insert(
                            END,
                            f"caramel pudding x{pudding_qty}\t\t\tRp. {pudding_price}\n\n",
                        )
                    else:
                        textStruk.insert(
                            END,
                            f"caramel pudding\t\t\tRp. {pudding_price}\n\n",
                        )

                textStruk.insert(END, "**\n")

                if hargadaribrunchvar.get() != "Rp 0":
                    textStruk.insert(
                        END, f"Harga dari makanan\t\t\tRp. {hargadaribrunch}\n\n"
                    )
                if hargadariminumanvar.get() != "Rp 0":
                    textStruk.insert(
                        END, f"Harga dari minuman\t\t\tRp. {hargadariminuman}\n\n"
                    )
                if hargadaridessertvar.get() != "Rp 0":
                    textStruk.insert(
                        END, f"Harga dari jajanan\t\t\tRp. {hargadaridessert}\n\n"
                    ) 

                # Tampilkan metode pembayaran yang dipilih di struk
                selected_method = dropdown.get()
                # Tampilkan harga dan kembalian di struk
                textStruk.insert(END, f"Sub Total\t\t\tRp. {subtotalItems}\n\n")
                textStruk.insert(END, f"Service Tax\t\t\tRp. {totaltax}\n\n")
                textStruk.insert(
                    END, f"Harga total\t\t\tRP. {subtotalItems + totaltax}\n\n"
                )
                if selected_method in ["QRIS", "Transfer"]:
                    bayar_pelanggan = subtotalItems + totaltax  # Jika metode pembayaran adalah QRIS atau Transfer, atur bayar_pelanggan secara otomatis
                    kembalian_pelanggan = 0  # Set kembalian pelanggan menjadi 0
                else:
                    try:
                        bayar_pelanggan = float(bayar_entry.get()) if bayar_entry.get() != "" else 0  # Mendapatkan nilai pembayaran dari input
                    except ValueError:
                        bayar_pelanggan = 0  # Jika terjadi kesalahan konversi, atur bayar_pelanggan ke 0
                    kembalian_pelanggan = kembalian2.cget("text")  # Mendapatkan nilai kembalian dari label


                textStruk.insert(END, f"{selected_method}\t\t\tRp. {bayar_pelanggan}\n\n")
                textStruk.insert(END, f"Kembalian\t\t\t{kembalian_pelanggan}\n\n")
                textStruk.insert(END, "**\n")

            else:
                messagebox.showerror("Error", "Tidak ada item yang dipilih")

        # batas fungsi cetak struk

        # awal fungsi simpan dalam perangkat
        def save():
            if textStruk.get(1.0, END) == "\n":
                pass
            else:
                # HANYA DALAM EXTENSION FILE .txt
                url = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
                if url == None:
                    pass
                else:

                    bill_data = textStruk.get(1.0, END)
                    url.write(bill_data)
                    url.close()
                    messagebox.showinfo("Informasi", "Struk Anda berhasil disimpan")

        # Batas fungsi simpan dalam perangkat

        # awal fungsi reset
        def reset():
            textStruk.delete(1.0, END)
            e_sandwich.set("0")
            e_croissant.set("0")
            e_waffle.set("0")
            e_lasagna.set("0")
            e_burger.set("0")
            e_omelets.set("0")
            e_samosa.set("0")
            e_avocadotoast.set("0")
            e_tomatosoup.set("0")

            e_americano.set("0")
            e_lemontea.set("0")
            e_mocha.set("0")
            e_espresso.set("0")
            e_vanillalatte.set("0")
            e_airmineral.set("0")
            e_fruitysmoothies.set("0")
            e_cappuchinocoffe.set("0")
            e_matchalatte.set("0")

            e_applepie.set("0")
            e_frenchfries.set("0")
            e_churros.set("0")
            e_cheesecake.set("0")
            e_icecream.set("0")
            e_donuts.set("0")
            e_chococupcake.set("0")
            e_saladbuah.set("0")
            e_pudding.set("0")

            # batas untuk variables

            textsandwich.config(state=DISABLED)
            textcroissant.config(state=DISABLED)
            textwaffle.config(state=DISABLED)
            textlasagna.config(state=DISABLED)
            textburger.config(state=DISABLED)
            textomelets.config(state=DISABLED)
            textsamosa.config(state=DISABLED)
            textavocadotoast.config(state=DISABLED)
            texttomatosoup.config(state=DISABLED)

            textamericano.config(state=DISABLED)
            textlemontea.config(state=DISABLED)
            textmocha.config(state=DISABLED)
            textespresso.config(state=DISABLED)
            textvanillalatte.config(state=DISABLED)
            textairmineral.config(state=DISABLED)
            textfruitysmoothies.config(state=DISABLED)
            textcappuchinocoffe.config(state=DISABLED)
            textmatchalatte.config(state=DISABLED)

            textapplepie.config(state=DISABLED)
            textfrenchfries.config(state=DISABLED)
            textchurros.config(state=DISABLED)
            textcheesecake.config(state=DISABLED)
            texticecream.config(state=DISABLED)
            textdonuts.config(state=DISABLED)
            textchococupcake.config(state=DISABLED)
            textsaladbuah.config(state=DISABLED)
            textpudding.config(state=DISABLED)


            var1.set(0)
            var2.set(0)
            var3.set(0)
            var4.set(0)
            var5.set(0)
            var6.set(0)
            var7.set(0)
            var8.set(0)
            var9.set(0)
            var10.set(0)
            var11.set(0)
            var12.set(0)
            var13.set(0)
            var14.set(0)
            var15.set(0)
            var16.set(0)
            var17.set(0)
            var18.set(0)
            var19.set(0)
            var20.set(0)
            var21.set(0)
            var22.set(0)
            var23.set(0)
            var24.set(0)
            var25.set(0)
            var26.set(0)
            var27.set(0)
            

            hargadariminumanvar.set("")
            hargadaribrunchvar.set("")
            hargadaridessertvar.set("")
            subtotalvar.set("")
            servicetaxvar.set("")
            totalcostvar.set("")
            taxvaluevar.set("")
            
            bayar_entry.delete(0, END)

        # batas fungsi reset

        # mengaktifkan fungsi entry menu makanan
        def sandwich():
            global clicked
            if clicked == False:
                var1.set(1)
                textsandwich.config(state=NORMAL)
                textsandwich.delete(0, END)
                textsandwich.focus()
                clicked = True
            else:
                var1.set(0)
                textsandwich.config(state=DISABLED)
                e_sandwich.set(0)
                clicked = False

        def croissant():
            global clickedcroissant
            if clickedcroissant == False:
                var2.set(1)
                textcroissant.config(state=NORMAL)
                textcroissant.delete(0, END)
                textcroissant.focus()
                clickedcroissant = True
            else:
                var2.set(0)
                textcroissant.config(state=DISABLED)
                e_croissant.set(0)
                clickedcroissant = False

        def waffle():
            global clickedwaffle
            if clickedwaffle == False:
                var3.set(1)
                textwaffle.config(state=NORMAL)
                textwaffle.delete(0, END)
                textwaffle.focus()
                clickedwaffle = True
            else:
                var3.set(0)
                textwaffle.config(state=DISABLED)
                e_waffle.set(0)
                clickedwaffle = False

        def lasagna():
            global clickedlasagna
            if clickedlasagna == False:
                var4.set(1)
                textlasagna.config(state=NORMAL)
                textlasagna.delete(0, END)
                textlasagna.focus()
                clickedlasagna = True
            else:
                var4.set(0)
                textlasagna.config(state=DISABLED)
                e_lasagna.set(0)
                clickedlasagna = False

        def burger():
            global clickedburger
            if clickedburger == False:
                var5.set(1)
                textburger.config(state=NORMAL)
                textburger.delete(0, END)
                textburger.focus()
                clickedburger = True
            else:
                var5.set(0)
                textburger.config(state=DISABLED)
                e_burger.set(0)
                clickedburger = False

        def omelets():
            global clickedomelets
            if clickedomelets == False:
                var6.set(1)
                textomelets.config(state=NORMAL)
                textomelets.delete(0, END)
                textomelets.focus()
                clickedomelets = True
            else:
                var6.set(0)
                textomelets.config(state=DISABLED)
                e_omelets.set(0)
                clickedomelets = False

        def samosa():
            global clickedsamosa
            if clickedsamosa == False:
                var7.set(1)
                textsamosa.config(state=NORMAL)
                textsamosa.delete(0, END)
                textsamosa.focus()
                clickedsamosa = True
            else:
                var7.set(0)
                textsamosa.config(state=DISABLED)
                e_samosa.set(0)
                clickedsamosa = False

        def avocadotoast():
            global clickedavocadotoast
            if clickedavocadotoast == False:
                var8.set(1)
                textavocadotoast.config(state=NORMAL)
                textavocadotoast.delete(0, END)
                textavocadotoast.focus()
                clickedavocadotoast = True
            else:
                var8.set(0)
                textavocadotoast.config(state=DISABLED)
                e_avocadotoast.set(0)
                clickedavocadotoast = False

        def tomatosoup():
            global clickedtomatosoup
            if clickedtomatosoup == False:
                var9.set(1)
                texttomatosoup.config(state=NORMAL)
                texttomatosoup.delete(0, END)
                texttomatosoup.focus()
                clickedtomatosoup = True
            else:
                var9.set(0)
                texttomatosoup.config(state=DISABLED)
                e_tomatosoup.set(0)
                clickedtomatosoup = False

        # batas mengaktifkan entry menu makanan

        # mengaktifkan entry menu minuman
        def americano():
            global clickedamericano
            if clickedamericano == False:
                var10.set(1)
                textamericano.config(state=NORMAL)
                textamericano.delete(0, END)
                textamericano.focus()
                clickedamericano = True
            else:
                var10.set(0)
                textamericano.config(state=DISABLED)
                e_americano.set(0)
                clickedamericano = False

        def lemontea():
            global clickedlemontea
            if clickedlemontea == False:
                var11.set(1)
                textlemontea.config(state=NORMAL)
                textlemontea.delete(0, END)
                textlemontea.focus()
                clickedlemontea = True
            else:
                var11.set(0)
                textlemontea.config(state=DISABLED)
                e_lemontea.set(0)
                clickedlemontea = False

        def mocha():
            global clickedmocha
            if clickedmocha == False:
                var12.set(1)
                textmocha.config(state=NORMAL)
                textmocha.delete(0, END)
                textmocha.focus()
                clickedmocha = True
            else:
                var12.set(0)
                textmocha.config(state=DISABLED)
                e_mocha.set(0)
                clickedmocha = False

        def espresso():
            global clickedespresso
            if clickedespresso == False:
                var13.set(1)
                textespresso.config(state=NORMAL)
                textespresso.delete(0, END)
                textespresso.focus()
                clickedespresso = True
            else:
                var13.set(0)
                textespresso.config(state=DISABLED)
                e_espresso.set(0)
                clickedespresso = False

        def vanillalatte():
            global clickedvanillalatte
            if clickedvanillalatte == False:
                var14.set(1)
                textvanillalatte.config(state=NORMAL)
                textvanillalatte.delete(0, END)
                textvanillalatte.focus()
                clickedvanillalatte = True
            else:
                var14.set(0)
                textvanillalatte.config(state=DISABLED)
                e_vanillalatte.set(0)
                clickedvanillalatte = False

        def airmineral():
            global clickedairmineral
            if clickedairmineral == False:
                var15.set(1)
                textairmineral.config(state=NORMAL)
                textairmineral.delete(0, END)
                textairmineral.focus()
                clickedairmineral = True
            else:
                var15.set(0)
                textairmineral.config(state=DISABLED)
                e_airmineral.set(0)
                clickedairmineral = False

        def fruitysmoothies():
            global clickedfruitysmoothies
            if clickedfruitysmoothies == False:
                var16.set(1)
                textfruitysmoothies.config(state=NORMAL)
                textfruitysmoothies.delete(0, END)
                textfruitysmoothies.focus()
                clickedfruitysmoothies = True
            else:
                var16.set(0)
                textfruitysmoothies.config(state=DISABLED)
                e_fruitysmoothies.set(0)
                clickedfruitysmoothies = False

        def cappuchinocoffe():
            global clickedcappuchinocoffe
            if clickedcappuchinocoffe == False:
                var17.set(1)
                textcappuchinocoffe.config(state=NORMAL)
                textcappuchinocoffe.delete(0, END)
                textcappuchinocoffe.focus()
                clickedcappuchinocoffe = True
            else:
                var17.set(0)
                textcappuchinocoffe.config(state=DISABLED)
                e_cappuchinocoffe.set(0)
                clickedcappuchinocoffe = False

        def matchalatte():
            global clickedcmatchalatte
            if clickedcmatchalatte == False:
                var18.set(1)
                textmatchalatte.config(state=NORMAL)
                textmatchalatte.delete(0, END)
                textmatchalatte.focus()
                clickedcmatchalatte = True
            else:
                var18.set(0)
                textmatchalatte.config(state=DISABLED)
                e_matchalatte.set(0)
                clickedcmatchalatte = False

        # batas mengaktifkan entry minuman

        # mengaktifkan entry menu jajanan
        def applepie():
            global clickedapplepie
            if clickedapplepie == False:
                var19.set(1)
                textapplepie.config(state=NORMAL)
                textapplepie.delete(0, END)
                textapplepie.focus()
                clickedapplepie = True
            else:
                var19.set(0)
                textapplepie.config(state=DISABLED)
                e_applepie.set(0)
                clickedonionring = False

        def frenchfries():
            global clickedfrenchfries
            if clickedfrenchfries == False:
                var20.set(1)
                textfrenchfries.config(state=NORMAL)
                textfrenchfries.delete(0, END)
                textfrenchfries.focus()
                clickedfrenchfries = True
            else:
                var20.set(0)
                textfrenchfries.config(state=DISABLED)
                e_frenchfries.set(0)
                clickedfrenchfries = False

        def churros():
            global clickedchurros
            if clickedchurros == False:
                var21.set(1)
                textchurros.config(state=NORMAL)
                textchurros.delete(0, END)
                textchurros.focus()
                clickedchurros = True
            else:
                var21.set(0)
                textchurros.config(state=DISABLED)
                e_churros.set(0)
                clickedchurros = False

        def cheesecake():
            global clickedcheesecake
            if clickedcheesecake == False:
                var22.set(1)
                textcheesecake.config(state=NORMAL)
                textcheesecake.delete(0, END)
                textcheesecake.focus()
                clickedcheesecake = True
            else:
                var22.set(0)
                textcheesecake.config(state=DISABLED)
                e_cheesecake.set(0)
                clickedcheesecake = False

        def icecream():
            global clickedicecream
            if clickedicecream == False:
                var23.set(1)
                texticecream.config(state=NORMAL)
                texticecream.delete(0, END)
                texticecream.focus()
                clickedicecream = True
            else:
                var23.set(0)
                texticecream.config(state=DISABLED)
                e_icecream.set(0)
                clickedicecream = False

        def donuts():
            global clickeddonuts
            if clickeddonuts == False:
                var24.set(1)
                textdonuts.config(state=NORMAL)
                textdonuts.delete(0, END)
                textdonuts.focus()
                clickeddonuts = True
            else:
                var24.set(0)
                textdonuts.config(state=DISABLED)
                e_donuts.set(0)
                clickeddonuts = False

        def chococupcake():
            global clickedchococupcake
            if clickedchococupcake == False:
                var25.set(1)
                textchococupcake.config(state=NORMAL)
                textchococupcake.delete(0, END)
                textchococupcake.focus()
                clickedchococupcake = True
            else:
                var25.set(0)
                textchococupcake.config(state=DISABLED)
                e_chococupcake.set(0)
                clickedchococupcake = False

        def saladbuah():
            global clickedsaladbuah
            if clickedsaladbuah == False:
                var26.set(1)
                textsaladbuah.config(state=NORMAL)
                textsaladbuah.delete(0, END)
                textsaladbuah.focus()
                clickedsaladbuah = True
            else:
                var26.set(0)
                textchococupcake.config(state=DISABLED)
                e_chococupcake.set(0)
                clickedsaladbuah = False

        def pudding():
            global clickedpudding
            if clickedpudding == False:
                var27.set(1)
                textpudding.config(state=NORMAL)
                textpudding.delete(0, END)
                textpudding.focus()
                clickedpudding = True
            else:
                var27.set(0)
                textpudding.config(state=DISABLED)
                e_pudding.set(0)
                clickedpudding = False

        # FRAME KIRI

        # Membuat frame kiri untuk menu cafe
        menuFrame = Frame(screen, bd=5, relief=RIDGE, bg="#42AAFF")
        menuFrame.pack(side=LEFT)

        hargaFrame = Frame(menuFrame, bd=5, relief=RIDGE, bg="#2196F3", pady=12)
        hargaFrame.pack(side=BOTTOM)

        bayarFrame = Frame(menuFrame, bd=5, relief=RIDGE, bg="#2196F3", pady=12)
        bayarFrame.pack(side=RIGHT)

        brunchFrame = LabelFrame(
            menuFrame,
            text=" Food ",
            font=("Castellar", 13, "bold"),
            bd=10,
            relief=RIDGE,
            fg="#2f2f2f",
            bg="#f6f6f6",
        )
        brunchFrame.pack(side=LEFT)

        minumanFrame = LabelFrame(
            menuFrame,
            text=" Drink ",
            font=("Castellar", 13, "bold"),
            bd=10,
            relief=RIDGE,
            fg="#2f2f2f",
            bg="#f6f6f6",
        )
        minumanFrame.pack(side=LEFT)

        dessertFrame = LabelFrame(
            menuFrame,
            text=" Dessert ",
            font=("Castellar", 13, "bold"),
            bd=10,
            relief=RIDGE,
            fg="#2f2f2f",
            bg="#f6f6f6",
        )
        dessertFrame.pack(side=LEFT)
        # batas frame kiri (menu cafe)

        # membuat tampilan daftar menu makanan
        sandwich = Checkbutton(
            brunchFrame,
            text=" Sandwich ",
            font=("Calibri", 10, "bold"),
            onvalue=1,
            offvalue=0,
            variable=var1,
            command=sandwich,
            bg="#f6f6f6",
        )
        sandwich.grid(row=0, column=0, sticky=W)

        croissant = Checkbutton(
            brunchFrame,
            text=" Croissant ",
            font=("Calibri", 10, "bold"),
            onvalue=1,
            offvalue=0,
            variable=var2,
            command=croissant,
            bg="#f6f6f6",
        )
        croissant.grid(row=1, column=0, sticky=W)

        waffle = Checkbutton(
            brunchFrame,
            text=" Classic Waffle ",
            font=("Calibri", 10, "bold"),
            onvalue=1,
            offvalue=0,
            variable=var3,
            command=waffle,
            bg="#f6f6f6",
        )
        waffle.grid(row=2, column=0, sticky=W)

        lasagna = Checkbutton(
            brunchFrame,
            text=" Lasagna ",
            font=("Calibri", 10, "bold"),
            onvalue=1,
            offvalue=0,
            variable=var4,
            command=lasagna,
            bg="#f6f6f6",
        )
        lasagna.grid(row=3, column=0, sticky=W)

        burger = Checkbutton(
            brunchFrame,
            text=" Burger ",
            font=("Calibri", 10, "bold"),
            onvalue=1,
            offvalue=0,
            variable=var5,
            command=burger,
            bg="#f6f6f6",
        )
        burger.grid(row=4, column=0, sticky=W)

        omelets = Checkbutton(
            brunchFrame,
            text=" Omelets ",
            font=("Calibri", 10, "bold"),
            onvalue=1,
            offvalue=0,
            variable=var6,
            command=omelets,
            bg="#f6f6f6",
        )
        omelets.grid(row=5, column=0, sticky=W)

        samosa = Checkbutton(
            brunchFrame,
            text=" Samosa ",
            font=("Calibri", 10, "bold"),
            onvalue=1,
            offvalue=0,
            variable=var7,
            command=samosa,
            bg="#f6f6f6",
        )
        samosa.grid(row=6, column=0, sticky=W)

        avocadotoast = Checkbutton(
            brunchFrame,
            text=" Avocado Toast",
            font=("Calibri", 10, "bold"),
            onvalue=1,
            offvalue=0,
            variable=var8,
            command=avocadotoast,
            bg="#f6f6f6",
        )
        avocadotoast.grid(row=7, column=0, sticky=W)

        tomatosoup = Checkbutton(
            brunchFrame,
            text=" Tomato Soup ",
            font=("Calibri", 10, "bold"),
            onvalue=1,
            offvalue=0,
            variable=var9,
            command=tomatosoup,
            bg="#f6f6f6",
        )
        tomatosoup.grid(row=8, column=0, sticky=W)

        # menambahkan fields entri untuk item brunch
        textsandwich = Entry(
            brunchFrame,
            font=("Calibri", "10", "bold"),
            bd=7,
            width=8,
            state=DISABLED,
            textvar=e_sandwich,
        )
        textsandwich.grid(row=0, column=1)

        textcroissant = Entry(
            brunchFrame,
            font=("Calibri", "10", "bold"),
            bd=7,
            width=8,
            state=DISABLED,
            textvar=e_croissant,
        )
        textcroissant.grid(row=1, column=1)

        textwaffle = Entry(
            brunchFrame,
            font=("Calibri", "10", "bold"),
            bd=7,
            width=8,
            state=DISABLED,
            textvar=e_waffle,
        )
        textwaffle.grid(row=2, column=1)

        textlasagna = Entry(
            brunchFrame,
            font=("Calibri", "10", "bold"),
            bd=7,
            width=8,
            state=DISABLED,
            textvar=e_lasagna,
        )
        textlasagna.grid(row=3, column=1)

        textburger = Entry(
            brunchFrame,
            font=("Calibri", "10", "bold"),
            bd=7,
            width=8,
            state=DISABLED,
            textvar=e_burger,
        )
        textburger.grid(row=4, column=1)

        textomelets = Entry(
            brunchFrame,
            font=("Calibri", "10", "bold"),
            bd=7,
            width=8,
            state=DISABLED,
            textvar=e_omelets,
        )
        textomelets.grid(row=5, column=1)

        textsamosa = Entry(
            brunchFrame,
            font=("Calibri", "10", "bold"),
            bd=7,
            width=8,
            state=DISABLED,
            textvar=e_samosa,
        )
        textsamosa.grid(row=6, column=1)

        textavocadotoast = Entry(
            brunchFrame,
            font=("Calibri", "10", "bold"),
            bd=7,
            width=8,
            state=DISABLED,
            textvar=e_avocadotoast,
        )
        textavocadotoast.grid(row=7, column=1)

        texttomatosoup = Entry(
            brunchFrame,
            font=("Calibri", "10", "bold"),
            bd=7,
            width=8,
            state=DISABLED,
            textvar=e_tomatosoup,
        )
        texttomatosoup.grid(row=8, column=1)

        # membuat tampilan daftar menu minuman
        americano = Checkbutton(
            minumanFrame,
            text="Americano",
            font=("Calibri", 10, "bold"),
            onvalue=1,
            offvalue=0,
            variable=var10,
            command=americano,
            bg="#f6f6f6",
        )
        americano.grid(row=0, column=0, sticky=W)

        lemontea = Checkbutton(
            minumanFrame,
            text="Lemon Tea",
            font=("Calibri", 10, "bold"),
            onvalue=1,
            offvalue=0,
            variable=var11,
            command=lemontea,
            bg="#f6f6f6",
        )
        lemontea.grid(row=1, column=0, sticky=W)

        mocha = Checkbutton(
            minumanFrame,
            text="Mocha",
            font=("Calibri", 10, "bold"),
            onvalue=1,
            offvalue=0,
            variable=var12,
            command=mocha,
            bg="#f6f6f6",
        )
        mocha.grid(row=2, column=0, sticky=W)

        espresso = Checkbutton(
            minumanFrame,
            text="Espresso",
            font=("Calibri", 10, "bold"),
            onvalue=1,
            offvalue=0,
            variable=var13,
            command=espresso,
            bg="#f6f6f6",
        )
        espresso.grid(row=3, column=0, sticky=W)

        vanillalatte = Checkbutton(
            minumanFrame,
            text="Vanilla Latte",
            font=("Calibri", 10, "bold"),
            onvalue=1,
            offvalue=0,
            variable=var14,
            command=vanillalatte,
            bg="#f6f6f6",
        )
        vanillalatte.grid(row=4, column=0, sticky=W)

        airmineral = Checkbutton(
            minumanFrame,
            text="Air Mineral",
            font=("Calibri", 10, "bold"),
            onvalue=1,
            offvalue=0,
            variable=var15,
            command=airmineral,
            bg="#f6f6f6",
        )
        airmineral.grid(row=5, column=0, sticky=W)

        fruitysmoothies = Checkbutton(
            minumanFrame,
            text="Smoothies",
            font=("Calibri", 10, "bold"),
            onvalue=1,
            offvalue=0,
            variable=var16,
            command=fruitysmoothies,
            bg="#f6f6f6",
        )
        fruitysmoothies.grid(row=6, column=0, sticky=W)

        cappuchinocoffe = Checkbutton(
            minumanFrame,
            text="Cappuchino Coffe",
            font=("Calibri", 10, "bold"),
            onvalue=1,
            offvalue=0,
            variable=var17,
            command=cappuchinocoffe,
            bg="#f6f6f6",
        )
        cappuchinocoffe.grid(row=7, column=0, sticky=W)

        matchalatte = Checkbutton(
            minumanFrame,
            text="Matcha Latte",
            font=("Calibri", 10, "bold"),
            onvalue=1,
            offvalue=0,
            variable=var18,
            command=matchalatte,
            bg="#f6f6f6",
        )
        matchalatte.grid(row=8, column=0, sticky=W)

        # menambahkan fields entri untuk item minuman
        textamericano = Entry(
            minumanFrame,
            font=("Calibri", "10", "bold"),
            bd=7,
            width=7,
            state=DISABLED,
            textvar=e_americano,
        )
        textamericano.grid(row=0, column=1)

        textlemontea = Entry(
            minumanFrame,
            font=("Calibri", "10", "bold"),
            bd=7,
            width=7,
            state=DISABLED,
            textvar=e_lemontea,
        )
        textlemontea.grid(row=1, column=1)

        textmocha = Entry(
            minumanFrame,
            font=("Calibri", "10", "bold"),
            bd=7,
            width=7,
            state=DISABLED,
            textvar=e_mocha,
        )
        textmocha.grid(row=2, column=1)

        textespresso = Entry(
            minumanFrame,
            font=("Calibri", "10", "bold"),
            bd=7,
            width=7,
            state=DISABLED,
            textvar=e_espresso,
        )
        textespresso.grid(row=3, column=1)

        textvanillalatte = Entry(
            minumanFrame,
            font=("Calibri", "10", "bold"),
            bd=7,
            width=7,
            state=DISABLED,
            textvar=e_vanillalatte,
        )
        textvanillalatte.grid(row=4, column=1)

        textairmineral = Entry(
            minumanFrame,
            font=("Calibri", "10", "bold"),
            bd=7,
            width=7,
            state=DISABLED,
            textvar=e_airmineral,
        )
        textairmineral.grid(row=5, column=1)

        textfruitysmoothies = Entry(
            minumanFrame,
            font=("Calibri", "10", "bold"),
            bd=7,
            width=7,
            state=DISABLED,
            textvar=e_fruitysmoothies,
        )
        textfruitysmoothies.grid(row=6, column=1)

        textcappuchinocoffe = Entry(
            minumanFrame,
            font=("Calibri", "10", "bold"),
            bd=7,
            width=7,
            state=DISABLED,
            textvar=e_cappuchinocoffe,
        )
        textcappuchinocoffe.grid(row=7, column=1)

        textmatchalatte = Entry(
            minumanFrame,
            font=("Calibri", "10", "bold"),
            bd=7,
            width=7,
            state=DISABLED,
            textvar=e_matchalatte,
        )
        textmatchalatte.grid(row=8, column=1)

        # membuat tampilan daftar menu dessert
        applepie = Checkbutton(
            dessertFrame,
            text="Apple Pie",
            font=("Calibri", 10, "bold"),
            onvalue=1,
            offvalue=0,
            variable=var19,
            command=applepie,
            bg="#f6f6f6",
        )
        applepie.grid(row=0, column=0, sticky=W)

        frenchfries = Checkbutton(
            dessertFrame,
            text="French Fries",
            font=("Calibri", 10, "bold"),
            onvalue=1,
            offvalue=0,
            variable=var20,
            command=frenchfries,
            bg="#f6f6f6",
        )
        frenchfries.grid(row=1, column=0, sticky=W)

        churros = Checkbutton(
            dessertFrame,
            text="Churros",
            font=("Calibri", 10, "bold"),
            onvalue=1,
            offvalue=0,
            variable=var21,
            command=churros,
            bg="#f6f6f6",
        )
        churros.grid(row=2, column=0, sticky=W)

        cheesecake = Checkbutton(
            dessertFrame,
            text="Cheese Cake",
            font=("Calibri", 10, "bold"),
            onvalue=1,
            offvalue=0,
            variable=var22,
            command=cheesecake,
            bg="#f6f6f6",
        )
        cheesecake.grid(row=3, column=0, sticky=W)

        icecream = Checkbutton(
            dessertFrame,
            text="Ice Cream",
            font=("Calibri", 10, "bold"),
            onvalue=1,
            offvalue=0,
            variable=var23,
            command=icecream,
            bg="#f6f6f6",
        )
        icecream.grid(row=4, column=0, sticky=W)

        donuts = Checkbutton(
            dessertFrame,
            text="Glazed Donuts",
            font=("Calibri", 10, "bold"),
            onvalue=1,
            offvalue=0,
            variable=var24,
            command=donuts,
            bg="#f6f6f6",
        )
        donuts.grid(row=5, column=0, sticky=W)

        chococupcake = Checkbutton(
            dessertFrame,
            text="Lemon Cupcake",
            font=("Calibri", 10, "bold"),
            onvalue=1,
            offvalue=0,
            variable=var25,
            command=chococupcake,
            bg="#f6f6f6",
        )
        chococupcake.grid(row=6, column=0, sticky=W)
        saladbuah = Checkbutton(
            dessertFrame,
            text="Salad Buah",
            font=("Calibri", 10, "bold"),
            onvalue=1,
            offvalue=0,
            variable=var26,
            command=saladbuah,
            bg="#f6f6f6",
        )
        saladbuah.grid(row=7, column=0, sticky=W)

        pudding = Checkbutton(
            dessertFrame,
            text="Caramel Pudding",
            font=("Calibri", 10, "bold"),
            onvalue=1,
            offvalue=0,
            variable=var27,
            command=pudding,
            bg="#f6f6f6",
        )
        pudding.grid(row=8, column=0, sticky=W)

        # menambahkan fields entri untuk item dessert
        textapplepie = Entry(
            dessertFrame,
            font=("Calibri", "10", "bold"),
            bd=7,
            width=7,
            state=DISABLED,
            textvar=e_applepie,
        )
        textapplepie.grid(row=0, column=1)

        textfrenchfries = Entry(
            dessertFrame,
            font=("Calibri", "10", "bold"),
            bd=7,
            width=7,
            state=DISABLED,
            textvar=e_frenchfries,
        )
        textfrenchfries.grid(row=1, column=1)

        textchurros = Entry(
            dessertFrame,
            font=("Calibri", "10", "bold"),
            bd=7,
            width=7,
            state=DISABLED,
            textvar=e_churros,
        )
        textchurros.grid(row=2, column=1)

        textcheesecake = Entry(
            dessertFrame,
            font=("Calibri", "10", "bold"),
            bd=7,
            width=7,
            state=DISABLED,
            textvar=e_cheesecake,
        )
        textcheesecake.grid(row=3, column=1)

        texticecream = Entry(
            dessertFrame,
            font=("Calibri", "10", "bold"),
            bd=7,
            width=7,
            state=DISABLED,
            textvar=e_icecream,
        )
        texticecream.grid(row=4, column=1)

        textdonuts = Entry(
            dessertFrame,
            font=("Calibri", "10", "bold"),
            bd=7,
            width=7,
            state=DISABLED,
            textvar=e_donuts,
        )
        textdonuts.grid(row=5, column=1)
        textchococupcake = Entry(
            dessertFrame,
            font=("Calibri", "10", "bold"),
            bd=7,
            width=7,
            state=DISABLED,
            textvar=e_chococupcake,
        )
        textchococupcake.grid(row=6, column=1)

        textsaladbuah = Entry(
            dessertFrame,
            font=("Calibri", "10", "bold"),
            bd=7,
            width=7,
            state=DISABLED,
            textvariable=e_saladbuah,
        )
        textsaladbuah.grid(row=7, column=1)

        textpudding = Entry(
            dessertFrame,
            font=("Calibri", "10", "bold"),
            bd=7,
            width=7,
            state=DISABLED,
            textvariable=e_pudding,
        )
        textpudding.grid(row=8, column=1)

        # FRAME KANAN

        # Membuat frame kanan untuk (Struk)
        rightFrame = Frame(screen, bd=5, relief=RIDGE)
        rightFrame.pack(side=RIGHT)

        strukFrame = Frame(rightFrame, bd=1, relief=RIDGE, bg="#f0f0f0")
        strukFrame.pack()

        buttonFrame = Frame(rightFrame, bd=2, relief=RIDGE)
        buttonFrame.pack()
        # Batas frame kanan (Struk)

        # membuat label harga dan kolom entrinya
        LabelHargadariBrunch = Label(
            hargaFrame,
            text="HARGA DARI BRUNCH",
            font=("Constantia", 8, "bold"),
            bg="#2196F3",
            fg="white",
        )
        LabelHargadariBrunch.grid(row=0, column=0)

        LabelHargadariMinuman = Label(
            hargaFrame,
            text="HARGA DARI MINUMAN",
            font=("Constantia", 8, "bold"),
            bg="#2196F3",
            fg="white",
        )
        LabelHargadariMinuman.grid(row=1, column=0)


        LabelHargadariDessert = Label(
            hargaFrame,
            text="HARGA DARI DESSERT ",
            font=("Constantia", 8, "bold"),
            bg="#2196F3",
            fg="white",
        )
        LabelHargadariDessert.grid(row=2, column=0)

        LabelSubTotal = Label(
            hargaFrame,
            text="SUB TOTAL",
            font=("Constantia", 8, "bold"),
            bg="#2196F3",
            fg="white",
        )
        LabelSubTotal.grid(row=0, column=2)

        LabelTax = Label(
            hargaFrame,
            text="Pajak" + " " + str(tax * 100) + "%",
            font=("Constantia", 8, "bold"),
            bg="#2196F3",
            fg="white",
        )
        LabelTax.grid(row=1, column=2)

       


        # Membuat tampilan Buttons struk (Tombol-tombol pada frame kanan)
        buttonTotal = Button(
            buttonFrame,
            text="Total",
            font=("arial", 8, "bold"),
            fg="#fefefe",
            bg="#5959FF",
            bd=3,
            padx=12,
            command=totalcost,
        )
        buttonTotal.grid(row=0, column=0)

        buttonStruk = Button(
            buttonFrame,
            text="Struk",
            font=("arial", 8, "bold"),
            fg="#fefefe",
            bg="#b38b59",
            bd=3,
            padx=12,
            command=struk,
        )
        buttonStruk.grid(row=0, column=1)

        buttonSimpan = Button(
            buttonFrame,
            text="Simpan",
            font=("arial", 8, "bold"),
            fg="#fefefe",
            bg="#b38b59",
            bd=3,
            padx=12,
            command=save,
        )
        buttonSimpan.grid(row=0, column=2)

        buttonReset = Button(
            buttonFrame,
            text="Reset",
            font=("arial", 8, "bold"),
            fg="#fefefe",
            bg="red",
            bd=3,
            padx=12,
            command=reset,
        )
        buttonReset.grid(row=0, column=4)

        # menentukan teks pada frame struk
        textStruk = Text(
            strukFrame, font=("arial", 8, "bold"), bd=2, width=36, height=34
        )
        textStruk.grid(row=0, column=0)

        def erase():
            screen.destroy()

        def nothing():
            pass

        def khaki():
            screen['bg'] = 'khaki'

        def grey():
            screen['bg'] = 'grey'

        def pink():
            screen['bg'] = 'pink'

        menubar = Menu(screen)

        # Submenu "Menu"
        submenu = Menu(menubar, tearoff=0)
        submenu.add_command(label='Quit', command=erase)
        menubar.add_cascade(label="Menu", menu=submenu)

        # Submenu "Produk"
        submenu_produk = Menu(menubar, tearoff=0)
        submenu_produk.add_command(label='Lihat Produk', command=nothing)
        menubar.add_cascade(label="Produk", menu=submenu_produk)

        # Submenu "Background"
        submenu2 = Menu(menubar, tearoff=0)
        submenu2.add_command(label='Khaki', command=khaki)
        submenu2.add_separator()
        submenu2.add_command(label='Grey', command=grey)
        submenu2.add_separator()
        submenu2.add_command(label='Pink', command=pink)
        menubar.add_cascade(label="Background", menu=submenu2)

        screen.config(menu=menubar)
        

        screen.mainloop()


# Memasukkan Gambar
background_image = PhotoImage(file="stelliva4.png")
background_label = Label(root, image=background_image, bg="#D9D9D9").place(x=80, y=60)

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading = Label(
    frame,
    text="Sign in",
    fg="#57a1f8",
    bg="white",
    font=("Microsoft YaHei UI Light", 23, "bold"),
)
heading.place(x=100, y=5)


##########---------------------------------------------------------
def on_enter(e):
    user.delete(0, "end")


def on_leave(e):
    name = user.get()
    if name == "":
        user.insert(0, "username")


user = Entry(
    frame,
    width=25,
    fg="black",
    border=0,
    bg="white",
    font=("Microsoft YaHei UI Light", 11),
)
user.place(x=30, y=80)
user.insert(0, "Username")
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)


##########---------------------------------------------------------
def on_enter(e):
    code.delete(0, "end")


def on_leave(e):
    code = user.get()
    if name == "":
        code.insert(0, "Password")


code = Entry(
    frame,
    width=25,
    fg="black",
    border=0,
    bg="white",
    font=("Microsoft YaHei UI Light", 11),
)
code.place(x=30, y=150)
code.insert(0, "Password")
code.bind("<FocusIn>", on_enter)
code.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

Button(
    frame,
    width=39,
    pady=7,
    text="Sign in",
    bg="#57a1f8",
    fg="white",
    border=0,
    command=signin,
).place(x=35, y=204)
label = Label(
    frame,
    text="Don't have an account?",
    fg="black",
    bg="white",
    font=("Microsoft YaHei UI Light", 9),
)
label.place(x=75, y=270)

sign_up = Button(
    frame, width=6, text="Sign up", border=0, bg="white", cursor="hand2", fg="#57a1f8"
)
sign_up.place(x=215, y=270)


root.mainloop()
 