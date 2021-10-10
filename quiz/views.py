# from django.shortcuts import render

# # Create your views here.

# from .serializers import Total_quizSerializer, OptionsSerializer, Questions_tableSerializer
# from .models import Total_quiz, Options, Questions_table
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.http import Http404, HttpResponse, FileResponse, StreamingHttpResponse
# from operator import itemgetter


# class TotalQuizApiView(APIView):
#     # permission_classes = [IsAuthenticated]

#     def get_object_id(self, quiz_id):
#         """
#         Method to get the feature table id
#         :param feature_list_id: string id
#         :return: FeatureTable data object
#         """
#         try:
#             return Total_quiz.objects.get(quiz_id=quiz_id)
#         except Total_quiz.DoesNotExist:
#             raise Http404

#     def get(self, request, quiz_id=None):
#         print("insideget")
#         result = dict()
#         response = {"CodeStatus": 400, "Result": result, "Status": False, "Messages": "Bad request"}
#         try:
#             if quiz_id:
#                 print("insideif:::")
#                 get_one_quiz_list = self.get_object_id(quiz_id)
#                 print("get_one", type(get_one_quiz_list))
#                 quiz_list = Total_quizSerializer(get_one_quiz_list)
#                 print("quiz_list:::", quiz_list)
#                 result = quiz_list.data
#                 print("result:::", result)
#                 response["Result"] = result
#             else:
#                 print("insideelse::")
#                 get_all_quiz_lists = Total_quiz.objects.all()
#                 print("get_all::", get_all_quiz_lists)
#                 quiz_list = Total_quizSerializer(get_all_quiz_lists, many=True)
#                 result = quiz_list.data
#                 result = sorted(result, key=itemgetter('quiz_id'))
#                 response["Result"] = result
#             response['CodeStatus'] = 200
#             response['Status'] = True
#             response['Messages'] = "Record fetched successfully"
#             return Response(response)

#         except Exception as error:
#             print("error::", error)
#             response["CodeStatus"] = 404
#             response["Messages"] = "record not found"
#             return Response(response)

#     def post(self, request):
#         result = dict()
#         response = {"CodeStatus": 400, "Result": result, "Status": False, "Messages": "Bad request"}
#         serializer = Total_quizSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             result = serializer.data
#             response["Result"] = result
#             response["CodeStatus"] = 201
#             response["Status"] = True
#             response["Messages"] = "Record created successfully"
#             return Response(response)

#         result = serializer.errors
#         response["Result"] = result
#         return Response(response)


# class QuestionsApiView(APIView):
#     # permission_classes = [IsAuthenticated]

#     def get_object_id(self, quiz_id):
#         """
#         Method to get the feature table id
#         :param feature_list_id: string id
#         :return: FeatureTable data object
#         """
#         try:
#             return Questions_table.objects.filter(quiz_id=quiz_id)
#         except Questions_table.DoesNotExist:
#             raise Http404

#     def get(self, request, quiz_id=None):
#         print("insideget")
#         result = dict()
#         response_data = list()
#         response = {"CodeStatus": 400, "Result": result, "Status": False, "Messages": "Bad request"}
#         try:
#             print("quiz_id::", quiz_id)
#             if quiz_id:
#                 print("insideif:::")
#                 get_one_ques_list = self.get_object_id(quiz_id)
#                 print("get_one", get_one_ques_list)
#                 questions_list = Questions_tableSerializer(get_one_ques_list, many = True)
#                 print("question_list:::", questions_list)
#                 for ques in list(questions_list.data):
#                    print("ques:::", ques)
#                    ques_data = dict(ques)
#                    response_data.append(ques_data)
#                 # for i in get_one_ques_list:
#                 #     get_one_ques_list = i["quest_str"]
#                 #     questions_list = Questions_tableSerializer(get_one_ques_list)
#                 #     print("ques_list:::", questions_list)
#                 # result = questions_list.data
#                 print("result:::", response_data)
#                 response["Result"] = response_data
#             else:
#                 print("insideelse::")
#                 get_all_questions_lists = Questions_table.objects.all()
#                 print("get_all::", get_all_questions_lists)
#                 questions_list = Questions_tableSerializer(get_all_questions_lists, many=True)
#                 result = questions_list.data
#                 print("result:::", result)
#                 result = sorted(result, key=itemgetter('quiz_id'))
#                 response["Result"] = result
#             response['CodeStatus'] = 200
#             response['Status'] = True
#             response['Messages'] = "Record fetched successfully"
#             return Response(response)

#         except Exception as error:
#             print("error::", error)
#             response["CodeStatus"] = 404
#             response["Messages"] = "record not found"
#             return Response(response)

#     def post(self, request):
#         result = dict()
#         response = {"CodeStatus": 400, "Result": result, "Status": False, "Messages": "Bad request"}
#         serializer = Questions_tableSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             result = serializer.data
#             response["Result"] = result
#             response["CodeStatus"] = 201
#             response["Status"] = True
#             response["Messages"] = "Record created successfully"
#             return Response(response)

#         result = serializer.errors
#         response["Result"] = result
#         return Response(response)


# class OptionsApiView(APIView):
#     # permission_classes = [IsAuthenticated]

#     def get_object_id(self, quiz_id):
#         """
#         Method to get the feature table id
#         :param feature_list_id: string id
#         :return: FeatureTable data object
#         """
#         try:
#             return Options.objects.filter(quiz_id=quiz_id)
#         except Options.DoesNotExist:
#             raise Http404

#     def get(self, request, quiz_id=None):
#         print("insideget")
#         result = dict()
#         response = {"CodeStatus": 400, "Result": result, "Status": False, "Messages": "Bad request"}
#         response_data = list()
#         try:
#             if quiz_id:
#                 print("insideif:::")
#                 get_one_options_list = self.get_object_id(quiz_id)
#                 print("get_one", get_one_options_list)
#                 options_list = OptionsSerializer(get_one_options_list, many=True)
#                 for opt in list(options_list.data):
#                    print("opt:::", opt)
#                    opt_data = dict(opt)
#                    response_data.append(opt_data)
#                 # for i in get_one_ques_list:
#                 #     get_one_ques_list = i["quest_str"]
#                 #     questions_list = Questions_tableSerializer(get_one_ques_list)
#                 #     print("ques_list:::", questions_list)
#                 # result = questions_list.data
#                 print("result:::", response_data)
#                 response["Result"] = response_data
#                 result = options_list.data
#                 response["Result"] = result
#             else:
#                 print("insideelse::")
#                 get_all_options_lists = Options.objects.all()
#                 print("get_all::", get_all_options_lists)
#                 options_list = OptionsSerializer(get_all_options_lists, many=True)
#                 result = options_list.data
#                 result = sorted(result, key=itemgetter('option_id'))
#                 response["Result"] = result
#             response['CodeStatus'] = 200
#             response['Status'] = True
#             response['Messages'] = "Record fetched successfully"
#             return Response(response)

#         except Exception as error:
#             print("error::", error)
#             response["CodeStatus"] = 404
#             response["Messages"] = "record not found"
#             return Response(response)

#     def post(self, request):
#         result = dict()
#         response = {"CodeStatus": 400, "Result": result, "Status": False, "Messages": "Bad request"}
#         # is_many = isinstance(request.data, list)
#         # try:
#         #     if is_many:
#         #         serializer = OptionsSerializer(data=request.data, many=True)
#         #         if serializer.is_valid():
#         #             serializer.save()
#         #             result = serializer.data
#         #             response["Result"] = result
#         #             response["CodeStatus"] = 201
#         #             response["Status"] = True
#         #             response["Messages"] = "Record created successfully"
#         #             return Response(response)
#         #         return Response(response)

#         #     else:
#         #         print("request data:::", request.data)
#         #         serializer = OptionsSerializer(data=request.data)
#         #         print("serializer::", serializer)
#         #         if serializer.is_valid():
#         #             serializer.save()
#         #             result = serializer.data
#         #             response["Result"] = result
#         #             response["CodeStatus"] = 201
#         #             response["Status"] = True
#         #             response["Messages"] = "Record created successfully"
#         #             return Response(response)
#         #         return Response(response)


#         serializer = OptionsSerializer(data=request.data, many=True)
#         if serializer.is_valid():
#             serializer.save()
#             result = serializer.data
#             response["Result"] = result
#             response["CodeStatus"] = 201
#             response["Status"] = True
#             response["Messages"] = "Record created successfully"
#             return Response(response)

#         result = serializer.errors
#         response["Result"] = result
#         return Response(response)        
