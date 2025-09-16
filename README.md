# 📚 E-commerce Kitob Do‘koni

**Loyiha tavsifi:**  
Bu loyiha kitob do‘koni uchun kichik **e-commerce tizimi** hisoblanadi. Loyihaning ikki asosiy qismi mavjud: **User taraf** (foydalanuvchi) va **Admin panel**.  

---

## 🔹 User taraf

Foydalanuvchilar quyidagi funksiyalarni bajarishi mumkin:  

1. **Kitoblarni ko‘rish**  
   - Foydalanuvchilar katalogdagi kitoblarni ko‘rib chiqadi.  

2. **Savatchaga qo‘shish (Cart)**  
   - Kitoblarni savatchaga qo‘shib, xarid qilishga tayyorlaydi.  

3. **Ro‘yxatdan o‘tish / Login**  
   - Xarid qilishdan oldin telefon raqam orqali ro‘yxatdan o‘tish yoki login qilish talab qilinadi.  

4. **Xarid qilish usullari**  
   - **Online to‘lov**: Agar to‘lov integratsiyasi mavjud bo‘lsa, foydalanuvchi platformada to‘lovni amalga oshiradi.  
   - **ID kod orqali**: Agar to‘lov tizimi yo‘q bo‘lsa, foydalanuvchiga 6–8 raqamli ID kod beriladi. Shu kod bilan kitobni do‘kondan olishi mumkin.  

> 💡 **Maslahat:** User interface foydalanuvchiga qulay va vizual bo‘lishi kerak.  

---

## 🔹 Admin panel

Admin panel quyidagi bo‘limlardan iborat:  

1. **Yangi kitoblarni yuklash**  
   - Kitob nomi, muallifi, narxi, soni va boshqa ma’lumotlar kiritiladi.  

2. **Hamma kitoblar bo‘limi**  
   - Barcha kitoblar ro‘yxati ko‘rinadi.  
   - Shu yerda admin:  
     - Kitobni tahrirlash (edit)  
     - O‘chirish (delete)  
     - Kitob sonini oshirish yoki kamaytirish  

3. **Sotib olingan kitoblar bo‘limi**  
   - Xarid qilingan kitoblar ro‘yxati ko‘rinadi.  
   - Agar foydalanuvchiga ID berilgan bo‘lsa, shu ID ham ko‘rinadi.  

4. **Qolmagan kitoblar bo‘limi**  
   - Sotilib tugagan kitoblar alohida ro‘yxatda ko‘rinadi.  

> 💡 **Maslahat:** Admin panel funksiyalari xavfsiz bo‘lishi uchun autentifikatsiya va ruxsatlar qo‘yilishi zarur.  

---

## ⚙️ Texnologiyalar

- **Backend:** FastAPI  
- **Database:** SQLAlchemy + PostgreSQL (yoki SQLite)  
- **Server:** Uvicorn  
- **Frontend:** HTML/CSS/JS yoki React/Vue (agar mavjud bo‘lsa) 