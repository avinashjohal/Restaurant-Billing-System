from tkinter import *
from twilio.rest import Client
from tkinter import filedialog, messagebox
import random
import time

# ----------------- All Functions --------------------------
# 1. Receipt Function.


def reset():
    textReceipt.delete(1.0, END)
    e_roti.set('0')
    e_daal.set('0')
    e_kadhi.set('0')
    e_sabji.set('0')
    e_fish.set('0')
    e_kebab.set('0')
    e_chawal.set('0')
    e_Mutton.set('0')
    e_Paneer.set('0')
    e_chicken.set('0')

    e_lassi.set('0')
    e_Tea.set('0')
    e_coffee.set('0')
    e_Faluda.set('0')
    e_Roohafza.set('0')
    e_Shikanjvi.set('0')
    e_colddrink.set('0')
    e_FruteJuice.set('0')
    e_Badammilk.set('0')
    e_SpecialWater.set('0')

    e_Egg.set('0')
    e_Kitkat.set('0')
    e_Oreo.set('0')
    e_Apple.set('0')
    e_Vanilla.set('0')
    e_Banana.set('0')
    e_Brownie.set('0')
    e_Pineapple.set('0')
    e_Chocolate.set('0')
    e_BlackForest.set('0')

    textroti.config(state=DISABLED)
    textdaal.config(state=DISABLED)
    textkadhi.config(state=DISABLED)
    textsabji.config(state=DISABLED)
    textfish.config(state=DISABLED)
    textkebab.config(state=DISABLED)
    textPaneer.config(state=DISABLED)
    textchicken.config(state=DISABLED)
    textMutton.config(state=DISABLED)
    textchawal.config(state=DISABLED)

    textlassi.config(state=DISABLED)
    textTea.config(state=DISABLED)
    textcoffee.config(state=DISABLED)
    textFaluda.config(state=DISABLED)
    textShikanjvi.config(state=DISABLED)
    textcolddrink.config(state=DISABLED)
    textRoohafza.config(state=DISABLED)
    textBadammilk.config(state=DISABLED)
    textFruteJuice.config(state=DISABLED)
    textSpecialWater.config(state=DISABLED)

    textEgg.config(state=DISABLED)
    textOreo.config(state=DISABLED)
    textApple.config(state=DISABLED)
    textKitkat.config(state=DISABLED)
    textVanilla.config(state=DISABLED)
    textBanana.config(state=DISABLED)
    textBrownie.config(state=DISABLED)
    textPineapple.config(state=DISABLED)
    textChocolate.config(state=DISABLED)
    textBlackForest.config(state=DISABLED)

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
    var28.set(0)
    var29.set(0)
    var30.set(0)

    costofdrinksvar.set('')
    costoffoodvar.set('')
    costofcakesvar.set('')
    subtotalvar.set('')
    servicetaxvar.set('')
    totalcostvar.set('')


def send():
    if textReceipt.get(1.0, END) == '\n':
        pass
    else:
        def send_msg():
            message = textarea.get(1.0, END)
            number = numberfield.get()
            account_SID = 'ACe6a977462be390261d7a2445d910ecec'
            auth_Token = '144f9884b49a17f4563afabcfc305b23'
            client = Client(account_SID, auth_Token)

            message = client.messages.create(
                body=message,
                from_='+15094368131',
                to=number
            )
            print(message.sid)
            messagebox.showinfo('Send Successfully',
                                'Message sent succesfully')

    root2 = Toplevel()
    root2.title("Send Bill")
    root2.config(bg='#1c0601')
    root2.geometry('485x620+50+50')

    logoImage = PhotoImage(file='image-logo.png')
    label = Label(root2, image=logoImage, bg='#1c0601')
    label.pack(pady=5)

    numberLabel = Label(root2, text='Mobile Number', font=(
        'candara', 18, 'bold underline'), bg='#1c0601', fg='white')
    numberLabel.pack(pady=5)

    numberfield = Entry(root2, font=('helvetica', 18, 'bold'), bd=3, width=24)
    numberfield.pack(pady=5)

    billLabel = Label(root2, text='Bill Details', font=(
        'candara', 18, 'bold underline'), bg='#1c0601', fg='white')
    billLabel.pack(pady=5)

    textarea = Text(root2, font=('arial', 12, 'bold'),
                    bd=3, width=42, height=14)
    textarea.pack(pady=5)

    textarea.insert(END, 'Receipt Ref:\t\t'+billnumber+'\t\t'+date+'\n\n')
    textarea.insert(
        END, '***********************************************************\n')
    if costoffoodvar.get() != '0 Rs':
        textarea.insert(END, f'Cost Of Food\t\t\t{priceofFood}Rs\n\n')
    if costofdrinksvar.get() != '0 Rs':
        textarea.insert(END, f'Cost Of Drinks\t\t\t{priceofDrinks}Rs\n\n')
    if costofcakesvar.get() != '0 Rs':
        textarea.insert(END, f'Cost Of Cakes\t\t\t{priceofCakes}Rs\n\n')
    textarea.insert(
        END, '----------------------------------------------------------\n')
    textarea.insert(END, f'Sub Total\t\t\t{subtotalofItems}Rs\n\n')
    textarea.insert(END, f'Service Tax\t\t\t{50}Rs\n\n')
    textarea.insert(END, f'Total Cost\t\t\t{subtotalofItems+50}Rs\n\n')

    sendButton = Button(root2, text='SEND', font=(
        'candara 16 bold'), bg='white', fg='#e33500', bd=5, relief=GROOVE, pady=1, padx=15, command=send_msg)
    sendButton.pack(pady=5)

    root2.mainloop()


def save():
    if textReceipt.get(1.0, END) == '\n':
        pass
    else:
        url = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
        if url == None:
            pass
        else:

            bill_data = textReceipt.get(1.0, END)
            url.write(bill_data)
            url.close()
            messagebox.showinfo(
                'Information', 'Your Bill Is Succesfully Saved')


def receipt():
    global billnumber, date
    if costoffoodvar.get() != '' or costofcakesvar.get() != '' or costofdrinksvar.get() != '':
        textReceipt.delete(1.0, END)
        x = random.randint(100, 10000)
        billnumber = 'BILL'+str(x)
        date = time.strftime('%d/%m/%Y')
        textReceipt.insert(END, 'Receipt Ref:\t\t'+billnumber+'\t\t'+date+'\n')
        textReceipt.insert(END, '*************************************\n')
        textReceipt.insert(END, 'Items:\t\tCost Of Items(Rs)\n')
        textReceipt.insert(END, '*************************************\n')

# Foods
        if e_roti.get() != '0':
            textReceipt.insert(END, f'Roti:\t\t\t{int(e_roti.get())*10}\n\n')

        if e_daal.get() != '0':
            textReceipt.insert(END, f'Daal:\t\t\t{int(e_daal.get())*20}\n\n')

        if e_kadhi.get() != '0':
            textReceipt.insert(END, f'Kadhi:\t\t\t{int(e_kadhi.get())*50}\n\n')

        if e_fish.get() != '0':
            textReceipt.insert(END, f'Fish:\t\t\t{int(e_fish.get())*100}\n\n')

        if e_sabji.get() != '0':
            textReceipt.insert(
                END, f'Sabji:\t\t\t{int(e_sabji.get()) * 50}\n\n')

        if e_kebab.get() != '0':
            textReceipt.insert(
                END, f'Kebab:\t\t\t{int(e_kebab.get()) * 100}\n\n')

        if e_chawal.get() != '0':
            textReceipt.insert(
                END, f'Chawal:\t\t\t{int(e_chawal.get()) * 20}\n\n')

        if e_Mutton.get() != '0':
            textReceipt.insert(
                END, f'Mutton:\t\t\t{int(e_Mutton.get()) * 120}\n\n')

        if e_Paneer.get() != '0':
            textReceipt.insert(
                END, f'Paneer:\t\t\t{int(e_Paneer.get()) * 140}\n\n')

        if e_chicken.get() != '0':
            textReceipt.insert(
                END, f'Chicken:\t\t\t{int(e_chicken.get()) * 150}\n\n')

# Drinks
        if e_lassi.get() != '0':
            textReceipt.insert(
                END, f'Lassi:\t\t\t{int(e_lassi.get()) * 20}\n\n')

        if e_Tea.get() != '0':
            textReceipt.insert(END, f'Tea:\t\t\t{int(e_Tea.get()) * 20}\n\n')

        if e_coffee.get() != '0':
            textReceipt.insert(
                END, f'Coffee:\t\t\t{int(e_coffee.get()) * 40}\n\n')

        if e_Faluda.get() != '0':
            textReceipt.insert(
                END, f'Faluda:\t\t\t{int(e_Faluda.get()) * 40}\n\n')

        if e_Shikanjvi.get() != '0':
            textReceipt.insert(
                END, f'Shikanjvi:\t\t\t{int(e_Shikanjvi.get()) * 40}\n\n')

        if e_colddrink.get() != '0':
            textReceipt.insert(
                END, f'Cold Drinks:\t\t\t{int(e_colddrink.get()) * 20}\n\n')

        if e_Roohafza.get() != '0':
            textReceipt.insert(
                END, f'Roohafza:\t\t\t{int(e_Roohafza.get()) * 50}\n\n')

        if e_FruteJuice.get() != '0':
            textReceipt.insert(
                END, f'Frute Juice:\t\t\t{int(e_FruteJuice.get()) * 80}\n\n')

        if e_Badammilk.get() != '0':
            textReceipt.insert(
                END, f'Badam Milk:\t\t\t{int(e_Badammilk.get()) * 100}\n\n')

        if e_SpecialWater.get() != '0':
            textReceipt.insert(
                END, f'Special Water:\t\t\t{int(e_SpecialWater.get()) * 50}\n\n')

# Cakes
        if e_Egg.get() != '0':
            textReceipt.insert(
                END, f'Egg Cake:\t\t\t{int(e_Egg.get()) * 500}\n\n')

        if e_Oreo.get() != '0':
            textReceipt.insert(
                END, f'Oreo Cake:\t\t\t{int(e_Oreo.get()) * 550}\n\n')

        if e_Apple.get() != '0':
            textReceipt.insert(
                END, f'Apple Cake:\t\t\t{int(e_Apple.get()) * 450}\n\n')

        if e_Kitkat.get() != '0':
            textReceipt.insert(
                END, f'Kitkat Cake:\t\t\t{int(e_Kitkat.get()) * 650}\n\n')

        if e_Vanilla.get() != '0':
            textReceipt.insert(
                END, f'Vanilla Cake:\t\t\t{int(e_Vanilla.get()) * 700}\n\n')

        if e_Banana.get() != '0':
            textReceipt.insert(
                END, f'Banana Cake:\t\t\t{int(e_Banana.get()) * 400}\n\n')

        if e_Brownie.get() != '0':
            textReceipt.insert(
                END, f'Brownie Cake:\t\t\t{int(e_Brownie.get()) * 550}\n\n')

        if e_Chocolate.get() != '0':
            textReceipt.insert(
                END, f'Chocolate Cake:\t\t\t{int(e_Chocolate.get()) * 650}\n\n')

        if e_Pineapple.get() != '0':
            textReceipt.insert(
                END, f'Pineapple Cake:\t\t\t{int(e_Pineapple.get()) * 800}\n\n')

        if e_BlackForest.get() != '0':
            textReceipt.insert(
                END, f'Black Forest Cake:\t\t\t{int(e_BlackForest.get()) * 950}\n\n')

        textReceipt.insert(END, '*************************************\n')
        if costoffoodvar.get() != '0 Rs':
            textReceipt.insert(END, f'Cost Of Food\t\t\t{priceofFood}Rs\n\n')
        if costofdrinksvar.get() != '0 Rs':
            textReceipt.insert(
                END, f'Cost Of Drinks\t\t\t{priceofDrinks}Rs\n\n')
        if costofcakesvar.get() != '0 Rs':
            textReceipt.insert(END, f'Cost Of Cakes\t\t\t{priceofCakes}Rs\n\n')

        textReceipt.insert(END, f'Sub Total\t\t\t{subtotalofItems}Rs\n\n')
        textReceipt.insert(END, f'Service Tax\t\t\t{50}Rs\n\n')
        textReceipt.insert(END, f'Total Cost\t\t\t{subtotalofItems+50}Rs\n\n')
        textReceipt.insert(END, '*************************************\n')

    else:
        messagebox.showerror('Error', 'No Item Is selected')


def totalcost():
    global priceofFood, priceofDrinks, priceofCakes, subtotalofItems
    if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or \
            var6.get() != 0 or var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or\
            var11.get() != 0 or var12.get() != 0 or var13.get() != 0 or var14.get() != 0 or var15.get() != 0 or \
            var16.get() != 0 or var17.get() != 0 or var18.get() != 0 or var19.get() != 0 or var20.get() != 0 or \
            var21.get() != 0 or var22.get() != 0 or var23.get() != 0 or var24.get() != 0 or var25.get() != 0 or\
            var26.get() != 0 or var27.get() != 0 or var28.get() != 0 or var29.get() != 0 or var30.get() != 0:

        item1 = int(e_roti.get())
        item2 = int(e_daal.get())
        item3 = int(e_kadhi.get())
        item4 = int(e_fish.get())
        item5 = int(e_sabji.get())
        item6 = int(e_kebab.get())
        item7 = int(e_chawal.get())
        item8 = int(e_Mutton.get())
        item9 = int(e_Paneer.get())
        item10 = int(e_chicken.get())

        item11 = int(e_lassi.get())
        item12 = int(e_Tea.get())
        item13 = int(e_coffee.get())
        item14 = int(e_Faluda.get())
        item15 = int(e_Shikanjvi.get())
        item16 = int(e_colddrink.get())
        item17 = int(e_Roohafza.get())
        item18 = int(e_FruteJuice.get())
        item19 = int(e_Badammilk.get())
        item20 = int(e_SpecialWater.get())

        item21 = int(e_Egg.get())
        item22 = int(e_Oreo.get())
        item23 = int(e_Apple.get())
        item24 = int(e_Kitkat.get())
        item25 = int(e_Vanilla.get())
        item26 = int(e_Banana.get())
        item27 = int(e_Brownie.get())
        item28 = int(e_Chocolate.get())
        item29 = int(e_Pineapple.get())
        item30 = int(e_BlackForest.get())

    priceofFood = (item1*10)+(item2*20)+(item3*50)+(item4*100) + (item5*50) + \
        (item6*100)+(item7*20)+(item8*120)+(item9*140)+(item10*150)

    priceofDrinks = (item11*20)+(item12*20)+(item13*40)+(item14*40) + \
        (item15*40)+(item16*20)+(item17*50) + \
        (item18*80)+(item19*100)+(item20*50)

    priceofCakes = (item21*500)+(item22*550)+(item23*450)+(item24*650)+(item25*700)+(item26*400)+(item27*550)+(item28*650)+(item29*800)\
        + (item30*950)

    costoffoodvar.set(str(priceofFood) + ' Rs')
    costofdrinksvar.set(str(priceofDrinks) + ' Rs')
    costofcakesvar.set(str(priceofCakes) + ' Rs')

    subtotalofItems = priceofFood+priceofDrinks+priceofCakes
    subtotalvar.set(str(subtotalofItems)+' Rs')

    servicetaxvar.set('50 Rs')

    totalcost = subtotalofItems+50
    totalcostvar.set(str(totalcost)+' Rs')


def roti():
    if var1.get() == 1:
        textroti.config(state=NORMAL)
        textroti.delete(0, END)
        textroti.focus()
    else:
        textroti.config(state=DISABLED)
        e_roti.set('0')


def daal():
    if var2.get() == 1:
        textdaal.config(state=NORMAL)
        textdaal.delete(0, END)
        textdaal.focus()

    else:
        textdaal.config(state=DISABLED)
        e_daal.set('0')


def kadhi():
    if var3.get() == 1:
        textkadhi.config(state=NORMAL)
        textkadhi.delete(0, END)
        textkadhi.focus()

    else:
        textkadhi.config(state=DISABLED)
        e_kadhi.set('0')


def fish():
    if var4.get() == 1:
        textfish.config(state=NORMAL)
        textfish.delete(0, END)
        textfish.focus()

    else:
        textfish.config(state=DISABLED)
        e_fish.set('0')


def sabji():
    if var5.get() == 1:
        textsabji.config(state=NORMAL)
        textsabji.focus()
        textsabji.delete(0, END)
    elif var5.get() == 0:
        textsabji.config(state=DISABLED)
        e_sabji.set('0')


def kebab():
    if var6.get() == 1:
        textkebab.config(state=NORMAL)
        textkebab.focus()
        textkebab.delete(0, END)
    elif var6.get() == 0:
        textkebab.config(state=DISABLED)
        e_kebab.set('0')


def chawal():
    if var7.get() == 1:
        textchawal.config(state=NORMAL)
        textchawal.focus()
        textchawal.delete(0, END)
    elif var7.get() == 0:
        textchawal.config(state=DISABLED)
        e_chawal.set('0')


def Mutton():
    if var8.get() == 1:
        textMutton.config(state=NORMAL)
        textMutton.focus()
        textMutton.delete(0, END)
    elif var8.get() == 0:
        textMutton.config(state=DISABLED)
        e_Mutton.set('0')


def Paneer():
    if var9.get() == 1:
        textPaneer.config(state=NORMAL)
        textPaneer.focus()
        textPaneer.delete(0, END)
    elif var9.get() == 0:
        textPaneer.config(state=DISABLED)
        e_Paneer.set('0')


def chicken():
    if var10.get() == 1:
        textchicken.config(state=NORMAL)
        textchicken.focus()
        textchicken.delete(0, END)
    elif var10.get() == 0:
        textchicken.config(state=DISABLED)
        e_chicken.set('0')


def lassi():
    if var11.get() == 1:
        textlassi.config(state=NORMAL)
        textlassi.focus()
        textlassi.delete(0, END)
    elif var11.get() == 0:
        textlassi.config(state=DISABLED)
        e_lassi.set('0')


def Tea():
    if var12.get() == 1:
        textTea.config(state=NORMAL)
        textTea.focus()
        textTea.delete(0, END)
    elif var12.get() == 0:
        textTea.config(state=DISABLED)
        e_Tea.set('0')


def coffee():
    if var13.get() == 1:
        textcoffee.config(state=NORMAL)
        textcoffee.focus()
        textcoffee.delete(0, END)
    elif var13.get() == 0:
        textcoffee.config(state=DISABLED)
        e_coffee.set('0')


def Faluda():
    if var14.get() == 1:
        textFaluda.config(state=NORMAL)
        textFaluda.focus()
        textFaluda.delete(0, END)
    elif var14.get() == 0:
        textFaluda.config(state=DISABLED)
        e_Faluda.set('0')


def Shikanjvi():
    if var15.get() == 1:
        textShikanjvi.config(state=NORMAL)
        textShikanjvi.focus()
        textShikanjvi.delete(0, END)
    elif var15.get() == 0:
        textShikanjvi.config(state=DISABLED)
        e_Shikanjvi.set('0')


def colddrink():
    if var16.get() == 1:
        textcolddrink.config(state=NORMAL)
        textcolddrink.focus()
        textcolddrink.delete(0, END)
    elif var16.get() == 0:
        textcolddrink.config(state=DISABLED)
        e_colddrink.set('0')


def Roohafza():
    if var17.get() == 1:
        textRoohafza.config(state=NORMAL)
        textRoohafza.focus()
        textRoohafza.delete(0, END)
    elif var17.get() == 0:
        textRoohafza.config(state=DISABLED)
        e_Roohafza.set('0')


def FruteJuice():
    if var18.get() == 1:
        textFruteJuice.config(state=NORMAL)
        textFruteJuice.focus()
        textFruteJuice.delete(0, END)
    elif var18.get() == 0:
        textFruteJuice.config(state=DISABLED)
        e_FruteJuice.set('0')


def Badammilk():
    if var19.get() == 1:
        textBadammilk.config(state=NORMAL)
        textBadammilk.focus()
        textBadammilk.delete(0, END)
    elif var19.get() == 0:
        textBadammilk.config(state=DISABLED)
        e_Badammilk.set('0')


def SpecialWater():
    if var20.get() == 1:
        textSpecialWater.config(state=NORMAL)
        textSpecialWater.focus()
        textSpecialWater.delete(0, END)
    elif var20.get() == 0:
        textSpecialWater.config(state=DISABLED)
        e_SpecialWater.set('0')


def EggCake():
    if var21.get() == 1:
        textEgg.config(state=NORMAL)
        textEgg.focus()
        textEgg.delete(0, END)
    elif var21.get() == 0:
        textEgg.config(state=DISABLED)
        e_Egg.set('0')


def OreoCake():
    if var22.get() == 1:
        textOreo.config(state=NORMAL)
        textOreo.focus()
        textOreo.delete(0, END)
    elif var22.get() == 0:
        textOreo.config(state=DISABLED)
        e_Oreo.set('0')


def AppleCake():
    if var23.get() == 1:
        textApple.config(state=NORMAL)
        textApple.focus()
        textApple.delete(0, END)
    elif var23.get() == 0:
        textApple.config(state=DISABLED)
        e_Apple.set('0')


def KitkatCake():
    if var24.get() == 1:
        textKitkat.config(state=NORMAL)
        textKitkat.focus()
        textKitkat.delete(0, END)
    elif var24.get() == 0:
        textKitkat.config(state=DISABLED)
        e_Kitkat.set('0')


def VanillaCake():
    if var25.get() == 1:
        textVanilla.config(state=NORMAL)
        textVanilla.focus()
        textVanilla.delete(0, END)
    elif var25.get() == 0:
        textVanilla.config(state=DISABLED)
        e_Vanilla.set('0')


def BananaCake():
    if var26.get() == 1:
        textBanana.config(state=NORMAL)
        textBanana.focus()
        textBanana.delete(0, END)
    elif var26.get() == 0:
        textBanana.config(state=DISABLED)
        e_Banana.set('0')


def BrownieCake():
    if var27.get() == 1:
        textBrownie.config(state=NORMAL)
        textBrownie.focus()
        textBrownie.delete(0, END)
    elif var27.get() == 0:
        textBrownie.config(state=DISABLED)
        e_Brownie.set('0')


def ChocolateCake():
    if var28.get() == 1:
        textChocolate.config(state=NORMAL)
        textChocolate.focus()
        textChocolate.delete(0, END)
    elif var28.get() == 0:
        textChocolate.config(state=DISABLED)
        e_Chocolate.set('0')


def PineAppleCake():
    if var29.get() == 1:
        textPineapple.config(state=NORMAL)
        textPineapple.focus()
        textPineapple.delete(0, END)
    elif var29.get() == 0:
        textPineapple.config(state=DISABLED)
        e_Pineapple.set('0')


def BlackForestCake():
    if var30.get() == 1:
        textBlackForest.config(state=NORMAL)
        textBlackForest.focus()
        textBlackForest.delete(0, END)
    elif var30.get() == 0:
        textBlackForest.config(state=DISABLED)
        e_BlackForest.set('0')


root = Tk()

root.geometry('1280x700+0+0')
root.resizable(0, 0)
root.wm_iconbitmap('restaurant-icon.ico')  # for tital icon
root.title('Restaurant Billing System created by Avinash')
# root.config(bg = "black") #Background color

# this code for background img [13,14,15-lines of code]
bg = PhotoImage(file="res-veg-black.gif")
my_lable = Label(root, image=bg)
my_lable.place(x=0, y=0, relheight=1, relwidth=1)

topframe = Frame(root, bd=4, relief=RIDGE, bg='#0a0200')
topframe.pack(side=TOP, pady=5)

LabelTitle = Label(topframe, text='RESTAURANT BILLING SYSTEM', font=(
    'candara', 30, 'bold'), fg='white', bg='#0f0300', width=30, pady=5)
LabelTitle.grid(row=0, column=0, padx=5, pady=3)

# frames
menuframe = Frame(root, bd=5, relief=RIDGE, bg='#0a0200')
menuframe.pack(side=LEFT, padx=10)

costFrame = Frame(menuframe, bd=3, relief=RIDGE, bg='#0a0200')
costFrame.pack(side=BOTTOM, pady=2, ipadx=56)

foodframe = LabelFrame(menuframe, text='Food Items       '+'      Cost', font=(
    'candara', 16, 'bold'), bd=3, relief=RIDGE, bg='white', fg='#E14D2A')
foodframe.pack(side=LEFT, ipadx=5)

drinksframe = LabelFrame(menuframe, text='Drinks Items          '+'         Cost', font=(
    'candara', 16, 'bold'), bd=3, relief=RIDGE, bg='white', fg='#E14D2A')
drinksframe.pack(side=LEFT, ipadx=5)

cakesframe = LabelFrame(menuframe, text='Cakes Items         '+'         Cost', font=(
    'candara', 16, 'bold'), bd=3, relief=RIDGE, bg='white', fg='#E14D2A')
cakesframe.pack(side=LEFT, ipadx=5)

# right frame
rightFrame = Frame(root, bd=8, relief=RIDGE, bg='#0a0200')
rightFrame.pack(side=RIGHT, padx=10)

calculatorframe = Frame(rightFrame, bd=2, relief=RIDGE)
calculatorframe.pack()

receiptFrame = Frame(rightFrame, bd=2, relief=RIDGE)
receiptFrame.pack()

buttonFrame = Frame(rightFrame, bd=2, relief=RIDGE)
buttonFrame.pack()

# variable
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
var28 = IntVar()
var29 = IntVar()
var30 = IntVar()

e_roti = StringVar()
e_daal = StringVar()
e_kadhi = StringVar()
e_fish = StringVar()
e_sabji = StringVar()
e_kebab = StringVar()
e_chawal = StringVar()
e_Mutton = StringVar()
e_Paneer = StringVar()
e_chicken = StringVar()

e_lassi = StringVar()
e_Tea = StringVar()
e_coffee = StringVar()
e_Faluda = StringVar()
e_Shikanjvi = StringVar()
e_colddrink = StringVar()
e_Roohafza = StringVar()
e_FruteJuice = StringVar()
e_Badammilk = StringVar()
e_SpecialWater = StringVar()

e_Egg = StringVar()
e_Oreo = StringVar()
e_Apple = StringVar()
e_Kitkat = StringVar()
e_Vanilla = StringVar()
e_Banana = StringVar()
e_Brownie = StringVar()
e_Chocolate = StringVar()
e_Pineapple = StringVar()
e_BlackForest = StringVar()

costoffoodvar = StringVar()
costofdrinksvar = StringVar()
costofcakesvar = StringVar()
subtotalvar = StringVar()
servicetaxvar = StringVar()
totalcostvar = StringVar()

e_roti.set('0')
e_daal.set('0')
e_kadhi.set('0')
e_fish.set('0')
e_sabji.set('0')
e_kebab.set('0')
e_chawal.set('0')
e_Mutton.set('0')
e_Paneer.set('0')
e_chicken.set('0')

e_lassi.set('0')
e_Tea.set('0')
e_coffee.set('0')
e_Faluda.set('0')
e_Shikanjvi.set('0')
e_colddrink.set('0')
e_Roohafza.set('0')
e_FruteJuice.set('0')
e_Badammilk.set('0')
e_SpecialWater.set('0')

e_Egg.set('0')
e_Oreo.set('0')
e_Apple.set('0')
e_Kitkat.set('0')
e_Vanilla.set('0')
e_Banana.set('0')
e_Brownie.set('0')
e_Chocolate.set('0')
e_Pineapple.set('0')
e_BlackForest.set('0')

# ---------------------------------food Items Section-------------------

roti = Checkbutton(foodframe, text="Roti", font=('candara', 16, 'bold'),
                   bg='white', fg='black', onvalue=1, offvalue=0, variable=var1, command=roti)
roti.grid(row=0, column=0, sticky=W)

daal = Checkbutton(foodframe, text="Daal", font=('candara', 16, 'bold'),
                   bg='white', fg='black', onvalue=1, offvalue=0, variable=var2, command=daal)
daal.grid(row=1, column=0, sticky=W)

kadhi = Checkbutton(foodframe, text="Kadhi", font=('candara', 16, 'bold'),
                    bg='white', fg='black', onvalue=1, offvalue=0, variable=var3, command=kadhi)
kadhi.grid(row=2, column=0, sticky=W)

fish = Checkbutton(foodframe, text="Fish", font=('candara', 16, 'bold'),
                   bg='white', fg='black', onvalue=1, offvalue=0, variable=var4, command=fish)
fish.grid(row=3, column=0, sticky=W)

sabji = Checkbutton(foodframe, text="Sabji", font=('candara', 16, 'bold'),
                    bg='white', fg='black', onvalue=1, offvalue=0, variable=var5, command=sabji)
sabji.grid(row=4, column=0, sticky=W)

kebab = Checkbutton(foodframe, text="Kebab", font=('candara', 16, 'bold'),
                    bg='white', fg='black', onvalue=1, offvalue=0, variable=var6, command=kebab)
kebab.grid(row=5, column=0, sticky=W)

chawal = Checkbutton(foodframe, text="Chawal", font=('candara', 16, 'bold'),
                     bg='white', fg='black', onvalue=1, offvalue=0, variable=var7, command=chawal)
chawal.grid(row=6, column=0, sticky=W)

Mutton = Checkbutton(foodframe, text="Mutton", font=('candara', 16, 'bold'),
                     bg='white', fg='black', onvalue=1, offvalue=0, variable=var8, command=Mutton)
Mutton.grid(row=7, column=0, sticky=W)

Paneer = Checkbutton(foodframe, text="Paneer", font=('candara', 16, 'bold'),
                     bg='white', fg='black', onvalue=1, offvalue=0, variable=var9, command=Paneer)
Paneer.grid(row=8, column=0, sticky=W)

chicken = Checkbutton(foodframe, text="Chicken", font=('candara', 16, 'bold'),
                      bg='white', fg='black', onvalue=1, offvalue=0, variable=var10, command=chicken)
chicken.grid(row=9, column=0, sticky=W)


# Entry Feild is for input quantity and Message Widget is showing price for Food Items.

textroti = Entry(foodframe, font=('candara', 16, 'bold'), bd=2,
                 width=5, state=DISABLED, textvariable=e_roti)
textroti.grid(row=0, column=1,)

priceroti = Message(foodframe, text='10Rs', justify='left',
                    font=('cambria', 10), bg='white')
priceroti .grid(row=0, column=2,)

textdaal = Entry(foodframe, font=('candara', 16, 'bold'), bd=2,
                 width=5, state=DISABLED, textvariable=e_daal)
textdaal.grid(row=1, column=1)

pricedaal = Message(foodframe, text='20Rs', justify='left',
                    font=('cambria', 10), bg='white')
pricedaal.grid(row=1, column=2,)

textkadhi = Entry(foodframe, font=('candara', 16, 'bold'),
                  bd=2, width=5, state=DISABLED, textvariable=e_kadhi)
textkadhi.grid(row=2, column=1)

pricekadhi = Message(foodframe, text='50Rs', justify='left',
                     font=('cambria', 10), bg='white')
pricekadhi.grid(row=2, column=2,)

textfish = Entry(foodframe, font=('candara', 16, 'bold'), bd=2,
                 width=5, state=DISABLED, textvariable=e_fish)
textfish.grid(row=3, column=1)

pricefish = Message(foodframe, text='100Rs', justify='left',
                    font=('cambria', 10), bg='white')
pricefish.grid(row=3, column=2)

textsabji = Entry(foodframe, font=('candara', 16, 'bold'),
                  bd=2, width=5, state=DISABLED, textvariable=e_sabji)
textsabji.grid(row=4, column=1)

pricesabji = Message(foodframe, text='50Rs', justify='left',
                     font=('cambria', 10), bg='white')
pricesabji.grid(row=4, column=2,)

textkebab = Entry(foodframe, font=('candara', 16, 'bold'),
                  bd=2, width=5, state=DISABLED, textvariable=e_kebab)
textkebab.grid(row=5, column=1)

pricekebab = Message(foodframe, text='100Rs', justify='left',
                     font=('cambria', 10), bg='white')
pricekebab.grid(row=5, column=2,)

textchawal = Entry(foodframe, font=('candara', 16, 'bold'),
                   bd=2, width=5, state=DISABLED, textvariable=e_chawal)
textchawal.grid(row=6, column=1)

pricechawal = Message(foodframe, text='20Rs', justify='left',
                      font=('cambria', 10), bg='white')
pricechawal.grid(row=6, column=2,)

textMutton = Entry(foodframe, font=('candara', 16, 'bold'),
                   bd=2, width=5, state=DISABLED, textvariable=e_Mutton)
textMutton.grid(row=7, column=1)

priceMutton = Message(foodframe, text='120Rs',
                      justify='left', font=('cambria', 10), bg='white')
priceMutton.grid(row=7, column=2,)

textPaneer = Entry(foodframe, font=('candara', 16, 'bold'),
                   bd=2, width=5, state=DISABLED, textvariable=e_Paneer)
textPaneer.grid(row=8, column=1)

pricePaneer = Message(foodframe, text='140Rs',
                      justify='left', font=('cambria', 10), bg='white')
pricePaneer.grid(row=8, column=2,)

textchicken = Entry(foodframe, font=('candara', 16, 'bold'),
                    bd=2, width=5, state=DISABLED, textvariable=e_chicken)
textchicken.grid(row=9, column=1)

pricechicken = Message(foodframe, text='150Rs',
                       justify='left', font=('cambria', 10), bg='white')
pricechicken.grid(row=9, column=2,)

# Drinks

lassi = Checkbutton(drinksframe, text="Lassi", font=('candara', 16, 'bold'),
                    bg='white', fg='black', onvalue=1, offvalue=0, variable=var11, command=lassi)
lassi.grid(row=0, column=0, sticky=W)

Tea = Checkbutton(drinksframe, text="Tea", font=('candara', 16, 'bold'),
                  bg='white', fg='black', onvalue=1, offvalue=0, variable=var12, command=Tea)
Tea.grid(row=1, column=0, sticky=W)

coffee = Checkbutton(drinksframe, text="Coffee", font=('candara', 16, 'bold'),
                     bg='white', fg='black', onvalue=1, offvalue=0, variable=var13, command=coffee)
coffee.grid(row=2, column=0, sticky=W)

Faluda = Checkbutton(drinksframe, text="Faluda", font=('candara', 16, 'bold'),
                     bg='white', fg='black', onvalue=1, offvalue=0, variable=var14, command=Faluda)
Faluda.grid(row=3, column=0, sticky=W)

Shikanjvi = Checkbutton(drinksframe, text="Shikanjvi", font=('candara', 16, 'bold'),
                        bg='white', fg='black', onvalue=1, offvalue=0, variable=var15, command=Shikanjvi)
Shikanjvi.grid(row=4, column=0, sticky=W)

colddrink = Checkbutton(drinksframe, text="Colddrinks", font=('candara', 16, 'bold'),
                        bg='white', fg='black', onvalue=1, offvalue=0, variable=var16, command=colddrink)
colddrink.grid(row=5, column=0, sticky=W)

Roohafza = Checkbutton(drinksframe, text="Roohafza", font=('candara', 16, 'bold'),
                       bg='white', fg='black', onvalue=1, offvalue=0, variable=var17, command=Roohafza)
Roohafza.grid(row=6, column=0, sticky=W)

FruteJuice = Checkbutton(drinksframe, text="FruteJuice", font=('candara', 16, 'bold'),
                         bg='white', fg='black', onvalue=1, offvalue=0, variable=var18, command=FruteJuice)
FruteJuice.grid(row=7, column=0, sticky=W)

Badammilk = Checkbutton(drinksframe, text="Badammilk", font=('candara', 16, 'bold'),
                        bg='white', fg='black', onvalue=1, offvalue=0, variable=var19, command=Badammilk)
Badammilk.grid(row=8, column=0, sticky=W)

SpecialWater = Checkbutton(drinksframe, text="SpecialWater", font=('candara', 16, 'bold'),
                           bg='white', fg='black', onvalue=1, offvalue=0, variable=var20, command=SpecialWater)
SpecialWater.grid(row=9, column=0, sticky=W)


# Entry Feild for Drink Items

textlassi = Entry(drinksframe, font=('candara', 16, 'bold'),
                  bd=2, width=5, state=DISABLED, textvariable=e_lassi)
textlassi.grid(row=0, column=1)

pricelassi = Message(drinksframe, text='20Rs',
                     justify='left', font=('cambria', 10), bg='white')
pricelassi.grid(row=0, column=2,)

textTea = Entry(drinksframe, font=('candara', 16, 'bold'),
                bd=2, width=5, state=DISABLED, textvariable=e_Tea)
textTea.grid(row=1, column=1)

priceTea = Message(drinksframe, text='20Rs', justify='left',
                   font=('cambria', 10), bg='white')
priceTea.grid(row=1, column=2,)

textcoffee = Entry(drinksframe, font=('candara', 16, 'bold'),
                   bd=2, width=5, state=DISABLED, textvariable=e_coffee)
textcoffee.grid(row=2, column=1)

pricecoffee = Message(drinksframe, text='40Rs',
                      justify='left', font=('cambria', 10), bg='white')
pricecoffee.grid(row=2, column=2,)

textFaluda = Entry(drinksframe, font=('candara', 16, 'bold'),
                   bd=2, width=5, state=DISABLED, textvariable=e_Faluda)
textFaluda.grid(row=3, column=1)

priceFaluda = Message(drinksframe, text='40Rs',
                      justify='left', font=('cambria', 10), bg='white')
priceFaluda.grid(row=3, column=2,)

textShikanjvi = Entry(drinksframe, font=('candara', 16, 'bold'),
                      bd=2, width=5, state=DISABLED, textvariable=e_Shikanjvi)
textShikanjvi.grid(row=4, column=1)

priceShikanjvi = Message(drinksframe, text='40Rs',
                         justify='left', font=('cambria', 10), bg='white')
priceShikanjvi.grid(row=4, column=2,)

textcolddrink = Entry(drinksframe, font=('candara', 16, 'bold'),
                      bd=2, width=5, state=DISABLED, textvariable=e_colddrink)
textcolddrink.grid(row=5, column=1)

pricecolddrink = Message(drinksframe, text='20Rs',
                         justify='left', font=('cambria', 10), bg='white')
pricecolddrink.grid(row=5, column=2,)

textRoohafza = Entry(drinksframe, font=('candara', 16, 'bold'),
                     bd=2, width=5, state=DISABLED, textvariable=e_Roohafza)
textRoohafza.grid(row=6, column=1)

priceRoohafza = Message(drinksframe, text='50Rs',
                        justify='left', font=('cambria', 10), bg='white')
priceRoohafza.grid(row=6, column=2,)

textFruteJuice = Entry(drinksframe, font=('candara', 16, 'bold'),
                       bd=2, width=5, state=DISABLED, textvariable=e_FruteJuice)
textFruteJuice.grid(row=7, column=1)

priceFruteJuice = Message(drinksframe, text='80Rs',
                          justify='left', font=('cambria', 10), bg='white')
priceFruteJuice.grid(row=7, column=2,)

textBadammilk = Entry(drinksframe, font=('candara', 16, 'bold'),
                      bd=2, width=5, state=DISABLED, textvariable=e_Badammilk)
textBadammilk.grid(row=8, column=1)

priceBadammilk = Message(drinksframe, text='100Rs',
                         justify='left', font=('cambria', 10), bg='white')
priceBadammilk.grid(row=8, column=2,)

textSpecialWater = Entry(drinksframe, font=('candara', 16, 'bold'),
                         bd=2, width=5, state=DISABLED, textvariable=e_SpecialWater)
textSpecialWater.grid(row=9, column=1)

priceSpecialWater = Message(
    drinksframe, text='50Rs', justify='left', font=('cambria', 10), bg='white')
priceSpecialWater.grid(row=9, column=2,)


# Cake
EggCake = Checkbutton(cakesframe, text="Egg", font=('candara', 16, 'bold'),
                      bg='white', fg='black', onvalue=1, offvalue=0, variable=var21, command=EggCake)
EggCake.grid(row=0, column=0, sticky=W)

OreoCake = Checkbutton(cakesframe, text="Oreo", font=('candara', 16, 'bold'),
                       bg='white', fg='black', onvalue=1, offvalue=0, variable=var22, command=OreoCake)
OreoCake.grid(row=1, column=0, sticky=W)

AppleCake = Checkbutton(cakesframe, text="Apple", font=('candara', 16, 'bold'),
                        bg='white', fg='black', onvalue=1, offvalue=0, variable=var23, command=AppleCake)
AppleCake.grid(row=2, column=0, sticky=W)

KitkatCake = Checkbutton(cakesframe, text="Kitkat", font=('candara', 16, 'bold'),
                         bg='white', fg='black', onvalue=1, offvalue=0, variable=var24, command=KitkatCake)
KitkatCake.grid(row=3, column=0, sticky=W)

VanillaCake = Checkbutton(cakesframe, text="Vanilla", font=('candara', 16, 'bold'),
                          bg='white', fg='black', onvalue=1, offvalue=0, variable=var25, command=VanillaCake)
VanillaCake.grid(row=4, column=0, sticky=W)

BananaCake = Checkbutton(cakesframe, text="Banana", font=('candara', 16, 'bold'),
                         bg='white', fg='black', onvalue=1, offvalue=0, variable=var26, command=BananaCake)
BananaCake.grid(row=5, column=0, sticky=W)

BrownieCake = Checkbutton(cakesframe, text="Brownie", font=('candara', 16, 'bold'),
                          bg='white', fg='black', onvalue=1, offvalue=0, variable=var27, command=BrownieCake)
BrownieCake.grid(row=6, column=0, sticky=W)

ChocolateCake = Checkbutton(cakesframe, text="Chocolate", font=(
    'candara', 16, 'bold'), bg='white', fg='black', onvalue=1, offvalue=0, variable=var28, command=ChocolateCake)
ChocolateCake.grid(row=7, column=0, sticky=W)

PineAppleCake = Checkbutton(cakesframe, text="Pineapple", font=(
    'candara', 16, 'bold'), bg='white', fg='black', onvalue=1, offvalue=0, variable=var29, command=PineAppleCake)
PineAppleCake.grid(row=8, column=0, sticky=W)

BlackForestCake = Checkbutton(cakesframe, text="BlackForest", font=(
    'candara', 16, 'bold'), bg='white', fg='black', onvalue=1, offvalue=0, variable=var30, command=BlackForestCake)
BlackForestCake.grid(row=9, column=0, sticky=W)

# Entry Feild for Cakes Items

textEgg = Entry(cakesframe, font=('candara', 16, 'bold'), bd=2,
                width=5, state=DISABLED, textvariable=e_Egg)
textEgg.grid(row=0, column=1)

priceEgg = Message(cakesframe, text='500Rs', justify='left',
                   font=('cambria', 10), bg='white')
priceEgg.grid(row=0, column=2,)

textOreo = Entry(cakesframe, font=('candara', 16, 'bold'),
                 bd=2, width=5, state=DISABLED, textvariable=e_Oreo)
textOreo.grid(row=1, column=1)

priceOreo = Message(cakesframe, text='550Rs', justify='left',
                    font=('cambria', 10), bg='white')
priceOreo.grid(row=1, column=2,)

textApple = Entry(cakesframe, font=('candara', 16, 'bold'),
                  bd=2, width=5, state=DISABLED, textvariable=e_Apple)
textApple.grid(row=2, column=1)

priceApple = Message(cakesframe, text='450Rs',
                     justify='left', font=('cambria', 10), bg='white')
priceApple.grid(row=2, column=2,)

textKitkat = Entry(cakesframe, font=('candara', 16, 'bold'),
                   bd=2, width=5, state=DISABLED, textvariable=e_Kitkat)
textKitkat.grid(row=3, column=1)

priceKitkat = Message(cakesframe, text='650Rs',
                      justify='left', font=('cambria', 10), bg='white')
priceKitkat.grid(row=3, column=2,)

textVanilla = Entry(cakesframe, font=('candara', 16, 'bold'),
                    bd=2, width=5, state=DISABLED, textvariable=e_Vanilla)
textVanilla.grid(row=4, column=1)

priceVanilla = Message(cakesframe, text='700Rs',
                       justify='left', font=('cambria', 10), bg='white')
priceVanilla.grid(row=4, column=2,)

textBanana = Entry(cakesframe, font=('candara', 16, 'bold'),
                   bd=2, width=5, state=DISABLED, textvariable=e_Banana)
textBanana.grid(row=5, column=1)

priceBanana = Message(cakesframe, text='400Rs',
                      justify='left', font=('cambria', 10), bg='white')
priceBanana.grid(row=5, column=2,)

textBrownie = Entry(cakesframe, font=('candara', 16, 'bold'),
                    bd=2, width=5, state=DISABLED, textvariable=e_Brownie)
textBrownie.grid(row=6, column=1)

priceBrownie = Message(cakesframe, text='550Rs',
                       justify='left', font=('cambria', 10), bg='white')
priceBrownie.grid(row=6, column=2,)

textChocolate = Entry(cakesframe, font=('candara', 16, 'bold'),
                      bd=2, width=5, state=DISABLED, textvariable=e_Chocolate)
textChocolate.grid(row=7, column=1)

priceChocolate = Message(cakesframe, text='650Rs',
                         justify='left', font=('cambria', 10), bg='white')
priceChocolate.grid(row=7, column=2,)

textPineapple = Entry(cakesframe, font=('candara', 16, 'bold'),
                      bd=2, width=5, state=DISABLED, textvariable=e_Pineapple)
textPineapple.grid(row=8, column=1)

pricePineapple = Message(cakesframe, text='800Rs',
                         justify='left', font=('cambria', 10), bg='white')
pricePineapple.grid(row=8, column=2,)

textBlackForest = Entry(cakesframe, font=(
    'candara', 16, 'bold'), bd=2, width=5, state=DISABLED, textvariable=e_BlackForest)
textBlackForest.grid(row=9, column=1)

priceBlackForest = Message(cakesframe, text='950Rs',
                           justify='left', font=('cambria', 10), bg='white')
priceBlackForest.grid(row=9, column=2,)

# Costlabels & entry fields
labelCostofFood = Label(costFrame, text='Cost of Food', font=(
    'candara', 16, 'bold'), bg='black', fg='white')
labelCostofFood.grid(row=0, column=0)

textCostofFood = Entry(costFrame, font=('candara', 16, 'bold'),
                       bd=2, width=10, state='readonly', textvariable=costoffoodvar)
textCostofFood.grid(row=0, column=1, padx=46, pady=5)

labelCostofDrinks = Label(costFrame, text='Cost of Drinks', font=(
    'candara', 16, 'bold'), bg='black', fg='white')
labelCostofDrinks.grid(row=1, column=0)

textCostofDrinks = Entry(costFrame, font=('candara', 16, 'bold'),
                         bd=2, width=10, state='readonly', textvariable=costofdrinksvar)
textCostofDrinks.grid(row=1, column=1, padx=46, pady=5)

labelCostofCakes = Label(costFrame, text='Cost of Cakes', font=(
    'candara', 16, 'bold'), bg='black', fg='white')
labelCostofCakes.grid(row=2, column=0)

textCostofCakes = Entry(costFrame, font=('candara', 16, 'bold'),
                        bd=2, width=10, state='readonly', textvariable=costofcakesvar)
textCostofCakes.grid(row=2, column=1, padx=46, pady=5)

labelSubTotal = Label(costFrame, text='Sub Total', font=(
    'candara', 16, 'bold'), bg='black', fg='white')
labelSubTotal.grid(row=0, column=2)

textSubTotal = Entry(costFrame, font=('candara', 16, 'bold'),
                     bd=2, width=10, state='readonly', textvariable=subtotalvar)
textSubTotal.grid(row=0, column=3, padx=46, pady=5)

labelServiceTax = Label(costFrame, text='Service Tax', font=(
    'candara', 16, 'bold'), bg='black', fg='white')
labelServiceTax.grid(row=1, column=2)

textServiceTax = Entry(costFrame, font=('candara', 16, 'bold'),
                       bd=2, width=10, state='readonly', textvariable=servicetaxvar)
textServiceTax.grid(row=1, column=3, padx=46, pady=5)

labelTotalCost = Label(costFrame, text='Total Cost', font=(
    'candara', 16, 'bold'), bg='black', fg='white')
labelTotalCost.grid(row=2, column=2)

textTotalCost = Entry(costFrame, font=('candara', 16, 'bold'),
                      bd=2, width=10, state='readonly', textvariable=totalcostvar)
textTotalCost.grid(row=2, column=3, padx=46, pady=5)


# Buttons

buttonTotal = Button(buttonFrame, text='Total', font=('candara', 14, 'bold'),
                     fg='white', bg='#FF1E00', bd=2, pady=2, padx=10, command=totalcost)
buttonTotal.grid(row=0, column=0)

buttonReceipt = Button(buttonFrame, text='Receipt', font=(
    'candara', 14, 'bold'), fg='black', bg='#00C957', bd=2, pady=2, padx=10, command=receipt)
buttonReceipt.grid(row=0, column=1)

buttonSave = Button(buttonFrame, text='Save', font=(
    'candara', 14, 'bold'), fg='black', bg='#00C957', bd=2, pady=2, padx=10, command=save)
buttonSave.grid(row=0, column=2)

buttonSend = Button(buttonFrame, text='Send', font=(
    'candara', 14, 'bold'), fg='black', bg='#00C957', bd=2, pady=2, padx=10, command=send)
buttonSend.grid(row=0, column=3)

buttonReset = Button(buttonFrame, text='Reset', font=(
    'candara', 14, 'bold'), fg='white', bg='#820000', bd=2, pady=2, padx=10, command=reset)
buttonReset.grid(row=0, column=4)

# Textarea for receipt
textReceipt = Text(receiptFrame, font=('candara', 14, 'bold'),
                   bd=5, bg='#FFF8BC', width=38, height=13)
textReceipt.grid(row=0, column=0)

# calculator
operator = ''  # hold values like 89+8,54+69+57


def buttonClick(numbers):
    global operator
    operator = operator+numbers
    calculatorField.delete(0, END)
    calculatorField.insert(END, operator)


def clear():
    global operator
    operator = ''
    calculatorField.delete(0, END)


def answer():
    global operator
    result = str(eval(operator))
    calculatorField.delete(0, END)
    calculatorField.insert(0, result)
    operator = ''


calculatorField = Entry(calculatorframe, font=(
    'lucida', 16, 'bold'), width=31, bd=4, bg='#FEFBF6')
calculatorField.grid(row=0, column=0, columnspan=4, ipady=3)

button7 = Button(calculatorframe, text='7', font=('candara', 16, 'bold'),
                 fg='black', bg='orange', width=8, command=lambda: buttonClick('7'))
button7.grid(row=1, column=0)
button8 = Button(calculatorframe, text='8', font=('candara', 16, 'bold'),
                 fg='black', bg='orange', width=8, command=lambda: buttonClick('8'))
button8.grid(row=1, column=1)
button9 = Button(calculatorframe, text='9', font=('candara', 16, 'bold'),
                 fg='black', bg='orange', width=8, command=lambda: buttonClick('9'))
button9.grid(row=1, column=2)
buttonplus = Button(calculatorframe, text='+', font=('candara', 16, 'bold'),
                    fg='black', bg='orange', width=8, command=lambda: buttonClick('+'))
buttonplus.grid(row=1, column=3)

button4 = Button(calculatorframe, text='4', font=('candara', 16, 'bold'),
                 fg='black', bg='orange', width=8, command=lambda: buttonClick('4'))
button4.grid(row=2, column=0)
button5 = Button(calculatorframe, text='5', font=('candara', 16, 'bold'),
                 fg='yellow', bg='red', width=8, command=lambda: buttonClick('5'))
button5.grid(row=2, column=1)
button6 = Button(calculatorframe, text='6', font=('candara', 16, 'bold'),
                 fg='yellow', bg='red', width=8, command=lambda: buttonClick('6'))
button6.grid(row=2, column=2)
buttonminus = Button(calculatorframe, text='-', font=('candara', 16, 'bold'),
                     fg='black', bg='orange', width=8, command=lambda: buttonClick('-'))
buttonminus.grid(row=2, column=3)

button1 = Button(calculatorframe, text='1', font=('candara', 16, 'bold'),
                 fg='black', bg='orange', width=8, command=lambda: buttonClick('1'))
button1.grid(row=3, column=0)
button2 = Button(calculatorframe, text='2', font=('candara', 16, 'bold'),
                 fg='yellow', bg='red', width=8, command=lambda: buttonClick('2'))
button2.grid(row=3, column=1)
button3 = Button(calculatorframe, text='3', font=('candara', 16, 'bold'),
                 fg='yellow', bg='red', width=8, command=lambda: buttonClick('3'))
button3.grid(row=3, column=2)
buttonmulti = Button(calculatorframe, text='*', font=('candara', 16, 'bold'),
                     fg='black', bg='orange', width=8, command=lambda: buttonClick('*'))
buttonmulti.grid(row=3, column=3)

buttonAns = Button(calculatorframe, text='Ans.', font=(
    'candara', 16, 'bold'), fg='black', bg='orange', width=8, command=answer)
buttonAns.grid(row=4, column=0)
buttonClear = Button(calculatorframe, text='Clear', font=(
    'candara', 16, 'bold'), fg='black', bg='orange', width=8, command=clear)
buttonClear.grid(row=4, column=1)
button0 = Button(calculatorframe, text='0', font=('candara', 16, 'bold'),
                 fg='black', bg='orange', width=8, command=lambda: buttonClick('0'))
button0.grid(row=4, column=2)
buttondevide = Button(calculatorframe, text='/', font=('candara', 16, 'bold'),
                      fg='black', bg='orange', width=8, command=lambda: buttonClick('/'))
buttondevide.grid(row=4, column=3)


root.mainloop()
