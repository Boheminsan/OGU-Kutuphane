PyQt5 ile Kütüphane Otomasyonu Projesi

Projenin kısaca tanımı:
Yazılım, bir kütüphanedeki kitapların kayıtlarını ve ödünç verilen kitapların süresini tutmaktadır. Temel iki özelliği vardır: Kitap veri tabanı ve Ödünç kitap verme. Kitap bölümünde kayıt, düzenleme ve silme; ödünç kitap bölümünde ise kayıt, süre uzatma ve teslim alma bölümleri bulunmaktadır.

Projenin geliştirilmesinde kullanılan programlar:
-Arayüz tasarımları için QtDesigner
-Arayüz dosyalarını python koduna dönüştürmek için komut satırı
-IDE olarak JetBrains PyCharm Community ve
-Microsoft Visual Studio 2015 Community,
-Küçük kod denemeleri için Idle,
-Notepad++ ve
-Mysql sunucusu için EasyPHP Devserver kullanılmıştır.
(Dipçe:Programların indirme bağlantıları en sonda verilecektir.)

Projenin tasarım aşamaları:

a)Veri tabanı Tasarımı: 
	Veri tabanı hakkında birçok farklı sql veri tabanı yönetim sistemi üzerinde düşünülmüş olup Sqlite ve MySQL sistemleri üzerinde çeşitli denemeler yapılmış ve kullanım pratikliği ve değişkenlerin elverişliliği gözetilerek MySQL veri tabanı kullanılmıştır.

b) GKA Tasarımı:
	Qt Designer ile tasarımlar yapıldıktan sonra (bkz Resim 5,6,7,8) kaydedilirse; Qt Designer tarafından projenin bulunduğu klasörde *.ui uzantılı dosyalar oluşturulur. Bu ui dosyaları XML tabanlı olduğu için not defteriyle kolayca düzenlenebilir. 
	Bu dosyaları py uzantılı python dosyalarına dönüştürmek için yönetici haklarıyla açılan bir MS-DOS komut satırında projenin klasörüne gidilip (cd ‘projenin bulunduğu klasör yolu’) pyuic komutu çalıştırılır. 
Örnek: pyuic5 hesap.ui -o hesap.py -x

Bu işlemi her ui dosyası için tekrarlamak gereklidir.

Programların bağlantıları ve yararlı kaynaklar:

QtDesigner: PyQt ile birlikte geliyor.
https://www.riverbankcomputing.com/software/pyqt/download5

Kaynaklar:
http://zetcode.com/gui/pyqt5/
https://github.com/baoboa/pyqt5
https://pythonspot.com/en/pyqt5/
http://nullege.com/codes/search/PyQt5
http://electronicsforu.com/resources/cool-stuff-misc/collection-51-free-ebooks-python-programming
http://pyankara.org/videolar/
http://www.istihza.com/

JetBrains PyCharm Community 
https://www.jetbrains.com/pycharm/download/

Microsoft Visual Studio 2015 Community
https://www.visualstudio.com/downloads/

Idle
Python ile birlikte geliyor.

Notepad++
https://notepad-plus-plus.org/download/v7.3.1.html

EasyPHP Devserver
http://www.easyphp.org/easyphp-devserver.php
