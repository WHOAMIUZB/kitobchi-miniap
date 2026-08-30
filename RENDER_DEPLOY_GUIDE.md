# 🚀 Mini App — Render’ga mustaqil joylash

Bu papka faqat **Mini App**ning o‘zini o‘z ichiga oladi — bot yoki web panel emas.
Render’da ishga tushirilgach, avtomatik **bepul HTTPS** oladi.

⚠️ **Muhim eslatma (albatta o‘qing):** bu Mini App o‘zining **alohida bazasini**
(`books.db`) yaratadi. Agar botingiz boshqa serverda (masalan Ubuntu VPS’ingizda)
ishlab tursa, ular **bir-biridan mustaqil, ikkita boshqa-boshqa baza** bo‘lib qoladi —
ya'ni foydalanuvchi Mini App’da ko‘rgan kitoblar, sevimlilar, XP — botdagi bilan
bog‘lanmaydi. Bu paket ko‘proq **sinov** yoki **kelajakda umumiy bazaga o‘tish**
uchun mo‘ljallangan.

---

## 1. GitHub’ga yuklang

```bash
cd kitoblar_miniapp_render
git init
git add .
git commit -m "Mini App uchun alohida deploy"
git remote add origin https://github.com/SIZNING_USERNAME/kitoblar-miniapp.git
git push -u origin main
```

## 2. Render’da Web Service yarating

1. [render.com](https://render.com)da ro‘yxatdan o‘ting / kiring
2. **New → Web Service**
3. GitHub repo’ingizni tanlang (`kitoblar-miniapp`)
4. Sozlamalar:
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python main.py`
   - **Plan**: kamida **Starter** (bepul rejada disk va doimiy ishlash yo‘q)

## 3. Environment Variables qo‘shing

Render dashboard’ida **Environment** bo‘limiga:

| Key | Value |
|---|---|
| `BOT_TOKEN` | Sizning bot tokeningiz (bot bilan **bir xil**) |
| `ADMIN_IDS` | `7861165622` |
| `BOOK_CLUB_CHAT_LINK` | Klub chat havolangiz |
| `DB_PATH` | `/var/data/books.db` |

## 4. Persistent Disk qo‘shing (bazani saqlab qolish uchun)

Render dashboard’ida: **Disks → Add Disk**
- **Name**: `kitoblar-data`
- **Mount Path**: `/var/data`
- **Size**: 1 GB (yetarli)

⚠️ Bu qadamni **o‘tkazib yubormang** — aks holda har deploy/qayta ishga tushirishda
barcha ma'lumotlar (foydalanuvchilar, XP, sevimlilar) o‘chib ketadi.

*(Alternativ: `render.yaml` fayli allaqachon shu sozlamalarni o‘z ichiga oladi — Render
"Blueprint" orqali joylashda avtomatik qo‘llaniladi: **New → Blueprint** → repo tanlang.)*

## 5. Deploy qiling

**Create Web Service** tugmasini bosing. Bir necha daqiqadan so‘ng Render sizga manzil beradi:
```
https://kitoblar-miniapp.onrender.com
```

Bu — sizning tayyor **HTTPS** Mini App manziling.

## 6. Botga ulash

Bot ishlab turgan serveringizda (`.env` faylida):
```env
MINIAPP_URL=https://kitoblar-miniapp.onrender.com
```

Botni qayta ishga tushiring.

---

## Baza muammosini butunlay hal qilish (tavsiya)

Agar Mini App va Bot **bir xil ma'lumotni** ko‘rishini xohlasangiz, ikki yo‘l bor:

1. **Eng oson**: Mini App’ni alohida joylashtirmang — VPS’ingizdagi asosiy loyihada
   (`main.py`) allaqachon bot + web panel + Mini App birga ishlaydi, faqat HTTPS uchun
   ngrok kerak (avvalgi xabarlarda to‘liq yozilgan)
2. **Professional yechim**: butun loyihani (bot ham) Render’ga ko‘chirish, bittagina
   Persistent Disk’dan foydalanish — shunda hammasi (bot, web panel, Mini App) bitta
   joyda, bitta bazada ishlaydi. Buni xohlasangiz, alohida to‘liq yo‘riqnoma tayyorlab
   beraman.
