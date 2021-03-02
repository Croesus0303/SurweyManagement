from django.db import models
import uuid

# Create your models here.

class bireyTanimaFormu(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    yas=models.IntegerField(blank=True, null=True)
    cinsiyet=CharField(max_length=20,blank=True, null=True)
    medeni_durum=models.CharField(max_length=20,blank=True, null=True)
    egitim_duzeyi=models.CharField(max_length=20,blank=True, null=True)
    meslek=models.CharField(max_length=20,blank=True, null=True)
    aylik_gelir=models.IntegerField(blank=True, null=True)
    alkol_kullanimi=models.CharField(max_length=20,blank=True, null=True)
    uyusturucu_madde_kullanimi=models.CharField(max_length=20,blank=True, null=True)
    uyusturucu_ismi_ve_miktari=models.CharField(max_length=20,blank=True, null=True)
    cocuklukta_psikiyatrist_basvuru_durumu=models.CharField(max_length=20,blank=True, null=True)
    psikolojik_yardim_suresi=models.CharField(max_length=20,blank=True, null=True)
    cocuklukta_hiperaktivite_tanisi=models.CharField(max_length=20,blank=True, null=True)
    hiperaktivite_ilac_tedavisi=models.CharField(max_length=20,blank=True, null=True)
    hiperaktivite_ilac_adi=models.CharField(max_length=20,blank=True, null=True)
    hiperaktivite_ilac_kullanim_suresi=models.CharField(max_length=20,blank=True, null=True)
    anne_egitim_durumu=models.CharField(max_length=20,blank=True, null=True)
    baba_egitim_durumu=models.CharField(max_length=20,blank=True, null=True)
    aile_tutumu=models.CharField(max_length=20,blank=True, null=True)

    def __str__(self):
        return self.id