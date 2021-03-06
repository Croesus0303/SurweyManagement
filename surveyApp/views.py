import gspread
from django.shortcuts import render
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('util/clientSecret.json', scope)
client = gspread.authorize(credentials)

birey_Tanima_Formu_Alanlari = ["custom-stacked-radio-yas", "custom-stacked-radio-cinsiyet",
                               "custom-stacked-radio-medeni",
                               "custom-stacked-radio-egitim", "meslek", "custom-stacked-radio-meslek-gelir",
                               "custom-stacked-radio-uyusturucu",
                               "uyusturucu-ismi-miktari", "custom-stacked-radio-psikiyatrist", "psikiyatrist-sure",
                               "custom-stacked-radio-hiper",
                               "custom-stacked-radio-hiper-ilac", "custom-stacked-radio-egitim-a",
                               "custom-stacked-radio-egitim-b", "custom-stacked-radio-alkol",
                               "custom-stacked-radio-tutum"]


# Create your views here.

def bireyTanimaFormu(request):
    if request.method == 'POST':
        try:
            formData = []
            # x = {
            #     "yas": request.POST.get("custom-stacked-radio-yas"),
            #     "cinsiyet": request.POST.get("custom-stacked-radio-cinsiyet"),
            #     "medeni": request.POST.get("custom-stacked-radio-medeni"),
            #     "egitim": request.POST.get("custom-stacked-radio-egitim"),
            #     "meslek": request.POST.get("meslek"),
            #     "gelir": request.POST.get("custom-stacked-radio-meslek-gelir"),
            #     "uyusturucu": request.POST.get("custom-stacked-radio-uyusturucu"),
            #     "ismi-miktari": request.POST.get("uyusturucu-ismi-miktari"),
            #     "psikiyatrist": request.POST.get("custom-stacked-radio-psikiyatrist"),
            #     "psikiyatrist-sure": request.POST.get("psikiyatrist-sure"),
            #     "hiper": request.POST.get("custom-stacked-radio-hiper"),
            #     "hiper-ilac": request.POST.get("custom-stacked-radio-hiper-ilac"),
            #     "egitim-a": request.POST.get("custom-stacked-radio-egitim-a"),
            #     "egitim-b": request.POST.get("custom-stacked-radio-egitim-b"),
            #     "alkol": request.POST.get("custom-stacked-radio-alkol"),
            #     "tutum": request.POST.get("custom-stacked-radio-tutum")
            #
            # }
            # y = json.dumps(x)

            # first column crsf token removed
            for val in list(dict(request.POST).values())[1:]:
                formData.append(val[0])

            sheet = client.open("BireyselTanıFormuCevaplar").sheet1

            sheet.append_row(formData, value_input_option='RAW')
            print(request.POST)

            # for key in y:
            #     formData.append([key, y[key]])
            #
            # sheet.update('A1', formData)

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
