#Hibrit Analiz ve Anomali Tespiti ile Sahte İş İlanlarının Belirlenmesi
Bu proje, sahte iş ilanlarını tespit etmek için metin tabanlı Doğal Dil İşleme (NLP) yöntemlerini, istatistiksel anomali tespiti teknikleriyle birleştiren hibrit bir denetim mekanizması geliştirmeyi amaçlamaktadır. Sistemin temel hedefi, sadece içeriğe değil, aynı zamanda ilanların yapısal davranışlarına da bakarak güvenilirliği artırmaktır.

#Proje Amacı
Mevcut NLP modelleri metin üzerinden yüksek başarı sağlasa da, dolandırıcılar metinleri manipüle ederek bu modelleri yanıltabilmektedir. Bu çalışma, içerikten bağımsız yapısal aykırılıkları (ilan sıklığı, eksik veri profili vb.) sürece dahil ederek daha sağlam bir savunma hattı oluşturur.

#Metodoloji ve İş Akışı
1. Metin Tabanlı Sınıflandırma
Projenin ilk aşamasında ilan başlığı, açıklaması ve gereksinimleri üzerinden bir modelleme yapılmıştır:

Ön İşleme: Metinler gürültüden arındırılmış ve temizlenmiştir.

Vektörleştirme: TF-IDF yöntemiyle kelimeler sayısal vektörlere dönüştürülmüştür.

Model: Logistic Regression (Sınıf ağırlıklı/Balanced) kullanılarak %95 başarı seviyesine ulaşılmıştır.

#2. İstatistiksel Anomali Tespiti
İlanların normal dışı davranışlarını yakalamak için şu özellikler analiz edilmektedir:

Sıklık Analizi: Belirli bir zaman diliminde aynı lokasyon veya şirketten çıkan aşırı ilan sayısı.

Eksik Veri Profili: Sahte ilanlarda şirket logosu veya web sitesi gibi alanların boş bırakılma eğilimi.

Algoritmalar: Veri kümesindeki uç değerleri izole etmek için Isolation Forest ve yerel sapmaları hesaplamak için Local Outlier Factor (LOF) kullanılmaktadır.

#Hedeflenen Sonuçlar
Yanıltıcı Alarmların Azaltılması: Sadece şüpheli kelimeler değil, aynı zamanda şüpheli davranış sergileyen ilanların önceliklendirilmesi.

Davranışsal Tespit: Metinler değiştirilse bile ilan verme sıklığı ve yapısal bozukluklar üzerinden tespitin sürdürülmesi.

#Kurulum ve Çalıştırma
Projeyi yerelinizde çalıştırmak için aşağıdaki adımları izleyebilirsiniz:

Depoyu klonlayın:
git clone https://github.com/SirSiestaLord/Ingilizce_Sahte_Is_Ilan_Belirleyici.git

Gerekli kütüphaneleri kurun:
pip install pandas scikit-learn

Modeli eğitin ve sonuçları görün:
python train.py

#Veri Kaynağı
Bu çalışmada Kaggle üzerinde yer alan "Real / Fake Job Posting Prediction" veri seti kullanılmıştır:https://www.kaggle.com/datasets/shivamb/real-or-fake-fake-jobposting-prediction
