from django.shortcuts import render

# Create your views here.

from .serializers import Total_quizSerializer, OptionsSerializer, Questions_tableSerializer
from .models import Total_quiz, Options, Questions_table
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404, HttpResponse, FileResponse, StreamingHttpResponse
from operator import itemgetter


class TotalQuizApiView(APIView):
    # permission_classes = [IsAuthenticated]

    def get_object_id(self, quiz_id):
        """
        Method to get the feature table id
        :param feature_list_id: string id
        :return: FeatureTable data object
        """
        try:
            return Total_quiz.objects.get(quiz_id=quiz_id)
        except Total_quiz.DoesNotExist:
            raise Http404

    def get(self, request, quiz_id=None):
        print("insideget")
        result = dict()
        response = {"CodeStatus": 400, "Result": result, "Status": False, "Messages": "Bad request"}
        try:
            if quiz_id:
                print("insideif:::")
                get_one_quiz_list = self.get_object_id(quiz_id)
                print("get_one", get_one_quiz_list)
                quiz_list = Total_quizSerializer(get_one_quiz_list)
                result = quiz_list.data
                response["Result"] = result
            else:
                print("insideelse::")
                get_all_quiz_lists = Total_quiz.objects.all()
                print("get_all::", get_all_quiz_lists)
                quiz_list = Total_quizSerializer(get_all_quiz_lists, many=True)
                result = quiz_list.data
                result = sorted(result, key=itemgetter('quiz_id'))
                response["Result"] = result
            response['CodeStatus'] = 200
            response['Status'] = True
            response['Messages'] = "Record fetched successfully"
            return Response(response)

        except Exception as error:
            print("error::", error)
            response["CodeStatus"] = 404
            response["Messages"] = "record not found"
            return Response(response)

    def post(self, request):
        result = dict()
        response = {"CodeStatus": 400, "Result": result, "Status": False, "Messages": "Bad request"}
        serializer = Total_quizSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            result = serializer.data
            response["Result"] = result
            response["CodeStatus"] = 201
            response["Status"] = True
            response["Messages"] = "Record created successfully"
            return Response(response)

        result = serializer.errors
        response["Result"] = result
        return Response(response)


class QuestionsApiView(APIView):
    # permission_classes = [IsAuthenticated]

    def get_object_id(self, quiz_id):
        """
        Method to get the feature table id
        :param feature_list_id: string id
        :return: FeatureTable data object
        """
        try:
            return list(Questions_table.objects.filter(quiz_id=quiz_id).values('quest_str'))
        except Questions_table.DoesNotExist:
            raise Http404

    def get(self, request, quiz_id=None):
        print("insideget")
        result = dict()
        response = {"CodeStatus": 400, "Result": result, "Status": False, "Messages": "Bad request"}
        try:
            if quiz_id:
                print("insideif:::")
                get_one_ques_list = self.get_object_id(quiz_id)
                print("get_one", get_one_ques_list)
                for i in get_one_ques_list:
                    get_one_ques_list = i["quest_str"]
                    questions_list = Questions_tableSerializer(get_one_ques_list)
                    result = questions_list.data
                    response["Result"] = result
            else:
                print("insideelse::")
                get_all_questions_lists = Questions_table.objects.all()
                print("get_all::", get_all_questions_lists)
                questions_list = Questions_tableSerializer(get_all_questions_lists, many=True)
                result = questions_list.data
                result = sorted(result, key=itemgetter('quiz_id'))
                response["Result"] = result
            response['CodeStatus'] = 200
            response['Status'] = True
            response['Messages'] = "Record fetched successfully"
            return Response(response)

        except Exception as error:
            print("error::", error)
            response["CodeStatus"] = 404
            response["Messages"] = "record not found"
            return Response(response)

    def post(self, request):
        result = dict()
        response = {"CodeStatus": 400, "Result": result, "Status": False, "Messages": "Bad request"}
        serializer = Questions_tableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            result = serializer.data
            response["Result"] = result
            response["CodeStatus"] = 201
            response["Status"] = True
            response["Messages"] = "Record created successfully"
            return Response(response)

        result = serializer.errors
        response["Result"] = result
        return Response(response)


class OptionsApiView(APIView):
    # permission_classes = [IsAuthenticated]

    def get_object_id(self, option_id):
        """
        Method to get the feature table id
        :param feature_list_id: string id
        :return: FeatureTable data object
        """
        try:
            return Options.objects.get(option_id=option_id)
        except Options.DoesNotExist:
            raise Http404

    def get(self, request, option_id=None):
        print("insideget")
        result = dict()
        response = {"CodeStatus": 400, "Result": result, "Status": False, "Messages": "Bad request"}
        try:
            if option_id:
                print("insideif:::")
                get_one_options_list = self.get_object_id(option_id)
                print("get_one", get_one_options_list)
                options_list = OptionsSerializer(get_one_options_list)
                result = options_list.data
                response["Result"] = result
            else:
                print("insideelse::")
                get_all_options_lists = Options.objects.all()
                print("get_all::", get_all_options_lists)
                options_list = OptionsSerializer(get_all_options_lists, many=True)
                result = options_list.data
                result = sorted(result, key=itemgetter('option_id'))
                response["Result"] = result
            response['CodeStatus'] = 200
            response['Status'] = True
            response['Messages'] = "Record fetched successfully"
            return Response(response)

        except Exception as error:
            print("error::", error)
            response["CodeStatus"] = 404
            response["Messages"] = "record not found"
            return Response(response)

    def post(self, request):
        result = dict()
        response = {"CodeStatus": 400, "Result": result, "Status": False, "Messages": "Bad request"}
        serializer = OptionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            result = serializer.data
            response["Result"] = result
            response["CodeStatus"] = 201
            response["Status"] = True
            response["Messages"] = "Record created successfully"
            return Response(response)

        result = serializer.errors
        response["Result"] = result
        return Response(response)        
