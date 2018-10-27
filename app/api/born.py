from flask import jsonify, request, Blueprint
from app.api import api, ns
from flask_restplus import Resource, fields
from app.tables.models import Born, BornSchema, db
from app.api.custom_response import custom_response

born_fields = api.model('Born', {

})

born_schema = BornSchema(many=True)

@ns.route('/born', methods=['GET', 'POST'])
class ListBorn(Resource):
    def get(self):
        queryset = Born.query.all()
        queryset = born_schema.dump(queryset).data
        return jsonify({
            'data' : queryset,
            'message' : 'Query OK',
            'error' : False
        }) 

    @api.doc(body=born_fields)
    def post(self):
        data = request.get_json(force=True)
        if data:
            try:
                queryset = Born()
                queryset.nama_bayi = data['nama_bayi']
                queryset.tempat_lahir = data['tempat_lahir']
                queryset.tanggal_lahir = data['tanggal_lahir']
                queryset.jam_lahir = data['jam_lahir']
                queryset.berat_badan = data['berat_badan']
                queryset.jenis_kelamin = data['jenis_kelamin']
                queryset.nama_ayah = data['nama_ayah']
                queryset.nama_ibu = data['nama_ibu']
                queryset.alamat = data['alamat']
                queryset.pelapor = data['pelapor']
                queryset.hubungan = data['hubungan']
                if queryset.save():
                    response = [
                        queryset.__serialize__()
                        ]
                    return custom_response(msg="Data Success Add!" ,data=response)
            except Exception as e:
                return custom_response(500, msg='There\'s an error!')

    def delete(self):
        queryset = Born.query.get()
        try:
            response = [
                queryset.__serialize__()
                ]
            if queryset.delete():
                return custom_response(data=response, msg='Data Successfully Delete !!')
        except Exception as e:
            return custom_response(500, msg='There\'s an error!')


