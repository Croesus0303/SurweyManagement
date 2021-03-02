from django.shortcuts import render


# Create your views here.

def bireyTanimaFormu(request):
    if request.method == 'POST':
        try:
            yas = request.POST.get("custom-stacked-radio-yas")
            cinsiyet = request.POST.get("custom-stacked-radio-cinsiyet")
            medeni_durum = request.POST.get("custom-stacked-radio-medeni")
            egitim = request.POST.get("custom-stacked-radio-egitim")
            meslek = request.POST.get("meslek")
            gelir = request.POST.get("custom-stacked-radio-meslek-gelir")
            uyusturucu_kullanimi = request.POST.get("custom-stacked-radio-uyusturucu")
            uyusturucu_ismi_miktari = request.POST.get("uyusturucu-ismi-miktari")
            psikiyatrist_durumu = request.POST.get("custom-stacked-radio-psikiyatrist")
            psikiyatrist_sure = request.POST.get("psikiyatrist-sure")
            hiperaktivite_durumu = request.POST.get("custom-stacked-radio-hiper")
            hiperaktivite_ilac_durumu = request.POST.get("custom-stacked-radio-hiper-ilac")
            anne_egitim = request.POST.get("custom-stacked-radio-egitim-a")
            baba_egitim = request.POST.get("custom-stacked-radio-egitim-b")
            alkol = request.POST.get("custom-stacked-radio-alkol")
            aile_tutumu = request.POST.get("custom-stacked-radio-tutum")
            print(request.POST)

            # aşağıdaki gibi bussiness logic'ler eklenebilir
            # if len(name) <= 0:
            #     logger.error(_("Name cannot be 0 or less characters. Account email : {}").format(request.user.id))
            #     return custom_error_result_with_success_code_200_ajax(_("Name cannot be 0 or less characters"))

            # if len(surname) <= 0:
            #     logger.error(_("Surname cannot be 0 or less characters. Account email : {}").format(request.user.id))
            #     return custom_error_result_with_success_code_200_ajax(_("Surname cannot be 0 or less characters"))

            # if not re.search(regex_email, email):
            #     logger.error(_("Mail format invalid. Account email : {}").format(request.user.id))
            #     return custom_error_result_with_success_code_200_ajax(_("Mail format invalid"))

            # if not re.search(regex_phone, phone):
            #     logger.error(_("Phone format invalid. Account email : {}").format(request.user.id))
            #     return custom_error_result_with_success_code_200_ajax(_("Phone format invalid"))

            # if not re.search(regex_tax_number, tax_number):
            #     logger.error(_("Tax number format invalid. Account email : {}").format(request.user.id))
            #     return custom_error_result_with_success_code_200_ajax(_("Tax number format invalid"))
            return render(request, 'success_page.html')
        except Exception as e:
            # response_data['error'] = True
            # response_data['result'] = e.args[0]
            print(e)
    return render(request, 'birey_tanima_formu.html')
