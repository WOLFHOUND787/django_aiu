
# Сабақ 1: Django-мен танысу және алғашқы жоба жасау

**Сабақтың мақсаты:**  
Студенттерді Django негіздерімен таныстырып, фреймворкті орнатуды және қарапайым веб-қосымша жасауды үйрету.

---

### 1. Django орнату

1. **Python орнатылғанын тексеріңіз**. Python нұсқасын тексеру үшін келесі команданы орындаңыз:
   ```bash
   python --version
   ```
   Егер Python орнатылмаған болса, оны [ресми сайттан](https://www.python.org/) жүктеп, орнатыңыз.

2. **Жоба үшін виртуалды орта жасаңыз**:
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # Windows үшін: myenv\Scripts\activate
   ```

3. **Django орнатыңыз**:
   ```bash
   pip install django
   ```

4. **Django орнатылғанын тексеріңіз**:
   ```bash
   django-admin --version
   ```

---

### 2. Жоба жасау және серверді іске қосу

1. **Жаңа жоба жасаңыз**:
   ```bash
   django-admin startproject mysite
   ```

2. **Жоба қалтасына өтіп, серверді іске қосыңыз**:
   ```bash
   cd mysite
   python manage.py runserver
   ```

3. **Браузерді ашып** [http://127.0.0.1:8000/](http://127.0.0.1:8000/) мекенжайына кіріңіз, онда сіз Django-ның сәлемдесу бетін көресіз.

---

### 3. Алғашқы қосымшаны жасау

1. **Жаңа қосымша жасаңыз**:
   ```bash
   python manage.py startapp blog
   ```

2. **Қосымшаны тіркеңіз** `settings.py` файлында. `'blog'` атауын `INSTALLED_APPS` бөліміне қосыңыз.

---

### 4. URL және View-мен жұмыс

1. **Қарапайым View функциясын жасаңыз**:
   `blog/views.py` файлын ашып, келесі функцияны жасаңыз:
   ```python
   from django.http import HttpResponse

   def home(request):
       return HttpResponse("Менің сайтыма қош келдіңіз!")
   ```

2. **Маршрутты баптаңыз**:
   `mysite/urls.py` файлына келесі жолды қосыңыз:
   ```python
   from blog import views

   urlpatterns = [
       path('', views.home),
   ]
   ```

3. **Серверді қайта іске қосыңыз** және браузерде басты бетке өтіңіз. Енді басты бетте "Менің сайтыма қош келдіңіз!" хабарламасы көрсетіледі.

---

### Практикалық тапсырма

1. "О нас" бетін жасап, жобаңыз туралы ақпаратты қайтару үшін жаңа View жасаңыз.
2. "О нас" беті үшін жаңа маршрутты баптаңыз.
3. Блог қосымшасын жасап, оны сайтқа қосыңыз.
