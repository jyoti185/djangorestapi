import task.models
from task.models import EmployeeModels
from task.serializers import EmployeeSerializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.generic import View
from django.http import HttpResponse
import io
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.db.utils import IntegrityError


@method_decorator(csrf_exempt, name='dispatch')
class EmployeeDetails(View):
    def post(self, request):

        b_data = request.body
        strm_data = io.BytesIO(b_data)
        dict_data = JSONParser().parse(strm_data)
        ps = EmployeeSerializers(data=dict_data)
        try:

            if ps.is_valid():
                ps.save()
                message = {"Success": "Record stored successfully"}
            else:
                message = {"errors": ps.errors}
        except IntegrityError:
            message = {"errors": "This Email id Already Exits"}
        json_data = JSONRenderer().render(message)
        return HttpResponse(json_data, content_type="application/json")

    def get(self, request, email=None):
        emp_email = email
        if emp_email:
            try:
                single_emp_details = EmployeeModels.objects.get(email=emp_email)
                serializer = EmployeeSerializers(single_emp_details)
                json_data = JSONRenderer().render(serializer.data)

            except EmployeeModels.DoesNotExist:
                message = {"errors": "This email id is not available Please Provide only valid email"}
                json_data = JSONRenderer().render(message)
            return HttpResponse(json_data, content_type="application/json")

        else:
            query_set = EmployeeModels.objects.all()
            serializer = EmployeeSerializers(query_set, many=True)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type="application/json")

    def put(self, request, email=None):
        emp_email = email
        b_data = request.body
        strm_data = io.BytesIO(b_data)
        dict_1 = JSONParser().parse(strm_data)
        if emp_email:
            try:
                res = EmployeeModels.objects.get(email=emp_email)
                ps = EmployeeSerializers(res, dict_1, partial=True)
                if ps.is_valid():
                    ps.save()
                    message = {"errors": "Details update successfully"}
                else:
                    message = {"errors": ps.errors}
            except EmployeeModels.DoesNotExist:
                message = {"errors": "Invalid Email please provide valid email "}

        else:
            message = {"errors": "please provide valid email to update the details"}
        json_data = JSONRenderer().render(message)
        return HttpResponse(json_data, content_type="application/json")

    def delete(self, request, email=None):
        emp_email = email
        if emp_email:
            try:
                EmployeeModels.objects.get(email=emp_email).delete()
                message = {"success": "data deleted successfully"}
            except EmployeeModels.DoesNotExist:
                message = {"errors": "This email id is not available"}
        else:
            message = {"errors": "please provide valid email to delete the details"}
        json_data = JSONRenderer().render(message)
        return HttpResponse(json_data, content_type="application/json")
