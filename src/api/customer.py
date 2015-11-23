# -*- coding: utf-8 -*-

from flask import Blueprint, Response, request
from flask.ext.restful import Resource

from dao.domain import Customer
from dao.database import Session
from utils.json_utils import JsonUtil
import json

from datetime import datetime

class RestApi(Resource):
     
    def __init__(self):
        self.session = Session()
#     
# class BuildApi(Resource):
#     
#     def __init__(self):
#         self.session = Session()
#     
#     def get(self, oid):
#         customer = self.session.query(Customer).filter(id==oid).first()
#         return Response(JsonUtil.objectToJson(build), mimetype='application/json')
#     
#     def delete(self, oid):
#         try:
#             Build.query.filter(Build.id == oid).delete()
#             db_session.commit()
#             return True, 204
#         except Exception as e:
#             print e
#             return '', 500
#         
#     def put(self, oid):
#         build = json.loads(request.data, object_hook=Build.decode)
# 
#         try:
#             build = db_session.merge(build)
#             db_session.commit()
#         except Exception as e:
#            #TODO: log exception
#            print e
#         return JsonUtil.objectToJson(build), 201
#     

class BuildListApi(RestApi):
    
    def get(self):
        customers = self.session.query(Customer).all()
        return customers, 200

        
#     def post(self):
#         build = json.loads(request.data, object_hook=Build.decode)
#         try:
#             db_session.add(build)
#             db_session.commit()
#         except Exception as e:
#             print e
#         return JsonUtil.objectToJson(build), 201
# #         return '', 201