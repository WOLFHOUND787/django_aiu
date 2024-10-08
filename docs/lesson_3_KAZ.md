
# Сабақ 3: Django-дағы Модельдер, миграциялар және мәліметтер базасымен жұмыс

**Сабақтың мақсаты:**  
Модельдер жасауды, миграциялар жасауды және Django-да мәліметтер базасымен жұмыс істеуді үйрену. Сабақтан кейін студенттер модельдер жасап, миграцияларды орындап, Django ORM арқылы мәліметтер базасымен жұмыс жасай алады.

---

### 1. Модельдер

Модель — бұл мәліметтер базасында сақталатын деректер құрылымының сипаттамасы. Django-да модельдер мәліметтер базасының кестелерін білдіреді және `models.py` файлында жасалады.

1. Қосымшадағы `models.py` файлын ашыңыз (мысалы, `blog/models.py`).

2. Келесі модельді қосыңыз:

```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
```

Бұл мысалда `Post` моделі тақырып (`title`), мазмұн (`content`) және жарияланған күн (`published_date`) өрістері бар кестені білдіреді.

---

### 2. Миграциялар

Миграциялар — бұл мәліметтер базасының құрылымын басқарудың тәсілі. Django модельдердегі өзгерістерге негізделген миграциялар жасайды.

1. Жаңа модель үшін миграцияларды жасаңыз:

   ```bash
   python manage.py makemigrations
   ```

2. Миграцияларды қолданып, кестені мәліметтер базасында жасаңыз:

   ```bash
   python manage.py migrate
   ```

---

### 3. Django ORM (Объектілік-реляциялық проекциялау)

Django мәліметтер базасымен SQL жазбай-ақ Python коды арқылы жұмыс істеуге мүмкіндік беретін қуатты ORM жүйесін ұсынады.

#### Django ORM негізгі функциялары:
- Мәліметтер базасына жазбалар енгізу.
- Жазбаларды жаңарту, жою және таңдау.
- Модельдер арасындағы қатынастармен жұмыс істеу (бір-біріне, көп-бірге және т.б.).

#### ORM-мен жұмыс істеу мысалы:

1. Python shell-ді іске қосыңыз:

   ```bash
   python manage.py shell
   ```

2. Жазба жасау:

   ```python
   from blog.models import Post
   post = Post.objects.create(title="Менің бірінші жазбам", content="Бұл менің бірінші жазбамның мазмұны")
   ```

3. Барлық жазбаларды алу:

   ```python
   posts = Post.objects.all()
   ```

4. Жазбаларды сүзу:

   ```python
   posts = Post.objects.filter(title__icontains="жазба")
   ```

5. Жазбаны жаңарту:

   ```python
   post = Post.objects.get(id=1)
   post.title = "Жаңартылған тақырып"
   post.save()
   ```

6. Жазбаны жою:

   ```python
   post = Post.objects.get(id=1)
   post.delete()
   ```

---

### 4. Әрі қарай не істеу керек?

1. Қосымшадағы `admin.py` файлын ашыңыз (мысалы, `blog/admin.py`) және модельді тіркеңіз:

   ```python
   from django.contrib import admin
   from .models import Post

   admin.site.register(Post)
   ```

2. Серверді іске қосып, суперпайдаланушы деректерімен [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) әкімшілік панельге кіріңіз.

3. Әкімшілік панельде сіз жасаған `Post` моделін көресіз және жазбаларды қосып, өңдеп, жоя аласыз.

---

### Практикалық тапсырма

1. Кітаптар туралы ақпаратты сақтау үшін модель жасаңыз: атауы, авторы, жарияланған күні, ISBN.
2. Миграциялар жасап, оларды қолданыңыз.
3. Django ORM арқылы модельмен жұмыс жасаңыз: бірнеше жазба жасап, оларды автор бойынша сұрыптаңыз, бір жазбаны жаңартыңыз және екіншісін жойыңыз.
