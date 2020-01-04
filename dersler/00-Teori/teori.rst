################################################
Temel Terimler ve Kisa Teorik Giris
################################################

Isbu belge basit uygulamalar yazmak için gerekli bir hayli kisa ve genel bir
giristir. Bir program yazarken en azindan burada yazanlari bilmeniz beklenir.
Ya da elinizdeki sorunu buradaki terminolojiyle ifade edebilmeniz beklenir.
Buradaki giris bir hayli yetersiz, ancak buradaki seanslari takip etmek için
gerekli.

Bu belgenin sonunda terimlerin ufak bir sozlukçe bulacaksiniz. Oradaki
tanimlar `FOLDOC <http://foldoc.org/>`_ sitesinden alinmistir.


Kodun Temel Birimleri
=========================

`ust duzey dil`_ olarak nitelenen bir programlama dilinde kod yazarken, en
temelde elimizde iki temel birim vardir:

- deger

- `islem`_

Islemsiz bir kod, sadece veridir, degersiz bir kod ise argumansiz islemlerden
olusacagindan, gunun sonunda bir hesaplama olmayacaktir. Her ikisi beraber
programlama dilinde yazilmis kodun temel unsurunu, ifadeyi, teskil ederler.

Deger kavrami bizim veri olarak tabir ettigimiz her sey olabilir. Islem
kavrami matematikteki kullanimindan ilham alsa da bilgi islem alaninda daha
farkli bir kullanima sahiptir.

Islem çikti verene denir. Bir çikti vermeyip programin durumunda bir
degisiklik yaratanlara usulen `prosedur`_ denir.

Ornegin `bash`, linux isletim sisteminin terminalinin kullandigi dil, genelde
prosedur yazmak için kullanilir. Temel amaç isletim sisteminin içinde
bulundugu durumu degistirmektir. Prosedurlerin uygulanmasi sonucu olusan
degisikliklere `yan etki`_ denir.

Sussman ve Abelson'a (Abelson, Harold, and Jay Sussman.  Structure and
Interpretation of Computer Programs. MIT Electrical Engineering and Computer
Science. London, 1996) gore bu basit unsurlarin disinda, guçlu her dil, bize
hem birlestirici unsurlar hem de soyutlama araçlari sunar.

Birlestirici unsurlar en temelde ifadeleri birlestirmeye yararlar.
Soyutlama araçlariysa programdaki tanili unsurlara erisimimizi saglarlar.

Bu unsurlar hemen hemen her programlama dilinde vardirlar, ve yeni programlama
dilleri ogrenirken bu unsurlarin neler oldugunu saptamak ogrenim surecinizi
kolaylastiracaktir. Yeni dil ogrenirken dolayisiyla sorulari soralim:

- Islemi, degerden ayiran nedir ?

- Ifadeleri birbirine baglayan nedir ?

- Ifadelere atifta bulunmamizi saglayan nedir ?



Islemin Unsurlari
-----------------


Islemin Girdi Degerleri
-----------------------

Arguman olarak da adlandirilir. Tipi yazili olabilir veya olmayabilir


Islemin Govdesi
---------------

Ifade, kodun deger ureten parçasidir. Ornegin:

.. code:: python

   a = 1 + 5
   print(a)

Yukaridaki ornekte ifade :code:`1+5`.

Yan etki :code:`a=Expr`.

Her dilde ifadeler bulunur. Ornegin asagida bir kaç dildeki ifadeleri 
karsilastiralim:


.. code:: python

    # python
    a = 2 + 1
    b = a + 3
    c = b + 4

.. code:: c++
    
    // c++
    int a = 2 + 1;
    int b = a + 3;
    int c = b + 4;

.. code:: clojure

    ;; clojure
    (
      def a (+ 1 2)
    )
    (
      def b (+ a 3 )
    )
    (
      def c (+ b 4)
    )


Hesap Yapma ve Programlama Dilleri
==================================


Programlama Dillerinde Pratikte Karsilasilan Dikatomiler
---------------------------------------------------------

Bu dikatomiler en temelde programlama dillerine belli bir perspektifle
bakabilmemizi saglayan basit kriterler. Bu kriterler dillerin kullanimindan
hareketle olustu. Onlari kesin birer duvar gibi degil, siyasal haritadaki
çizgiler gibi almak lazim, yani uygulamaya ve dilin yapisina ve o dilde
yazilan programlarin cinsine dair fikir veriyor olmasina ragmen, dili o
uygulamalara mahkum ediyor gibi dusunmemek lazim.



Ilk dikatomi, bazi ifadelerin ayricalikli olmasi veya her ifadenin ayni
unsurlardan mutesekkil olmasi yani homoikonik olmasi uzerine.

.. image:: ax1.png

Temelde su soruya verilen iki farkli cevabin sonucu bu dikatomi ortaya çikar:
"Bazi hesaplari dile getirmek digerlerine gore daha kolay olsun mu ?" Lisp
ailesine dahil olanlar "Yok canim ne alakasi var" derler. ALGOL ailesine dahil
olan diller "Tabi" derler. Her ikisinin de avantaji ve dezavantaji vardir.
Lisp ailesine dahil olanlar, verdikleri cevaba istinaden, geriye uyumluluk
konusunda çok avantajlidirlar. ALGOL ailesindekiler ise, yine verdikleri
cevaba istinaden, anlasilmasi daha kolaydir.

Ikinci dikatomi gelistirme suresi ile programin yurutum suresi.

.. image:: ax2.png

Klasik karsilastirma python ile c/c++ gibi diller arasinda yapilir. Genelde
programin hizli çalismasi için yapilan ekler, ornegin degiskenlerin tiplerini
yazmak gibi, programci tarafindan yazildigi için kodu uzatir.

Ornegin yukaridaki ornekte verdigimiz :code:`a = 1 + 2` ve :code:`int a = 1 +
2` ifadeleri ele alalim. Ayni isi yaptiklari bariz, ancak ikincisinde `a`
degiskeninin tipini biz el ile koda ekliyoruz. Bu gibi eklemeler programin
derlenerek, uygulama için optimize edilebilmesini sagliyor, ancak vakit
aliyorlar. Ilki argumanlarin tiplerinin uygunlugunu program yorumlayicisinin
kontrol etmesini talep ediyor, ki bu optimizasyon yok demek. 

Kodu yazma hiziniz artiyor ama programin yurutme hizi dusuyor. Ancak burada
soyle bir tercih yapiyoruz, bir program 0,0001 saniyede islemi yaparken digeri
0,01 saniyede yapiyor. Ilki tipleri el ile yazdigimiz program, ikincisi ise
yazmadigimiz program. Iki programda son kullanici açisindan fark edilmeyecek
derecede hizli islemi gerçeklestirdigi için genelde bagimsiz gelistiriciler
vakitlerinin çogunu ikinci tur programlama dillerinde program yazarak
geçiriyorlar. 

Bazi is kollari, performansin çok kritik oldugu alanlara tekabul ediyor,
ornegin finans, fiyati gorur gormez alis veya satis emrini vermeniz lazim, ve
bu sure ne kadar kisa olursa rakiplerinizin onune o kadar hizli geçme
ihtimaliniz var. Dolayisiyla her iki dilinde esasen geçerli kullanim alanlari
var. Genelde programlamaya tiplerin yazildigi diller ile baslanir, bu bazi
dogru pratikleri erken kazanmanya sizi zorlar.

Ucuncu dikatomi programlama dilinin safligi ve islevi arasindadir.

.. image:: ax3.png

Peyton Jones, buradaki dikatomiyi bir 
`videosunda <https://youtu.be/iSmkqocn0oQ>`_ guzel ozetliyor.


Hatalar
--------

Hatalar kaçinilmazdir. Onlarla bas etmek için paradigmalar ve gelistirme
sablonlari kullanilir.


Type
-----

Çok uzun mesele, kabaca ilgili degerlerin kurucu unsurlarini, ve uzerine
yapilabilecek islemleri belirleyen kume.


Glossaire
==========

.. _`ifade`: 

**Ifade**:
Ifade ust duzey dilde degerlendirilmesi halinde deger uretendir.

.. _`ust duzey dil`: 

**Ust Duzey Dil** (High level language):
Çevirici (assembly) dili uzerinde yukselen soyutlamari sunan programlama dili

.. _`islem`:

**Islem** (function):
Bir esleme/tekabul. Eger T ve D (tanim ve deger) kumeleri, f, :math:`f: T →
D`, seklinde ifadesini bulan, T ve D kumelerinin kartezyen çarpimindan olusan
:math:`{(t,d) | t ∈ T, d ∈ D}` kumesinin bir alt kumesidir, ve bu alt kumeye
islem denir. f alt kumesi su sartlari saglamak zorundadir:

- Her :math:`t ∈ T` için D kumesinde bir es/mutekabil bulunmak zorundadir.

- Herhangi :math:`t ∈ T`, için iki es, :math:`d1, d2 ∈ D` denk geliyorsa,
  esler birbirine esittir, :math:`d1=d2`


Bilgi islemdeki, karsili, yukaridaki tanimdan ilham alinmis olmasina ragmen,
daha esnektir. Bilgi islem baglaminda islemden soz ederken `tanim kumesi`_ ve
`deger kumesi` arasinda bir mutekabiliyet iliskisi kurandan bahsederiz.

.. _`prosedur`:

**Prosedur**:
Bir is yapmak için bir araya getirilmis bir dizi talimat. Islemlerden 
çikti degeri vermeyerek ayrisirlar. Olusturdugu `yan etki`_ dolayisiyla
uygulanirlar.

.. _`tanim kumesi`:

**Tanim kumesi** (domain):
Islemin uzerine tanimli oldugu elemanlari barindiran kume.

.. _`deger kumesi`:

**Deger kumesi** (codomain): 
Varis kumesi. Islemin sonucunda olusabilecek elemanlari barindiran kume.

.. _`aralik kumesi`:

**Aralik kumesi** (Goruntu): Elemanlari bir islemin sonucu olan kume, siklikla
`deger kumesi`_'nin bir alt kumesidir.

.. _`yan etki`:

**Yan Etki**:
Dilin programin durumunu degistirmek için uygulanan bir yapisi. En sık
gorulenler atama, girdi, çikti. Yan etkisi olmayan bir dil saf islevseldir, ki
uygulamasi yalnizca ifadelerin degerlendirilmesi uzerine kuruludur ve butun
alt ifadeler atif berrakligina sahiptir.

.. _`Atif Berrakligi`:

**Atif Berrakligi**:
Ifade I atif berrakligina, eger butun alt ifadeler degerleriyle
degistirildiginde kendi degerini kaybetmiyorsa, sahiptir.
