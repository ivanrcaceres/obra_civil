# -*- coding: utf-8 -*-
from builtins import len, range

from odoo import models, fields, api

class Detallecertificacion(models.Model):
    _name = "obra_civil.detallecertificado"

    # name = fields.Char(defaul='hola')
    product_id = fields.Many2one('product.product','Servicio')
    quantity = fields.Float('Cantidad')
    certificado_id = fields.Many2one('obra_civil.certificado')
    # fecha = fields.Datetime()
    # project = fields.Many2one('project.project')

class Certificacion(models.Model):
    _name = "obra_civil.certificado"

    fecha = fields.Datetime()
    project = fields.Many2one('project.project' , string='Proyecto')
    detallecertificado_ids = fields.One2many('obra_civil.detallecertificado', 'certificado_id' , string='Detalle')


    # este funcion envia todos los datos para los reportes de los certificados
    def hola(self):

        # aqui en a7 cargo todos los certificados de referencia a un solo proyecto
        a7 = self.env['obra_civil.certificado'].search([('project', '=', self.project.id)])


        # aqui en listadecertificados cargo todos los certificados de un proyecto excepto el actual certificado, porque el ultimo seria el avance actual de la obra
        listadecertificados = []
        for aux in a7:
            if aux.id == self.id:
                break
            # print(aux.id)
            # print(self.id)
            listadecertificados.append(aux)

        # for i in listadecertificados:
        #     for j in i.detallecertificado_ids:
        #         print (j.product_id.id)

        # aqui en servicios cargo servicios de la venta
        servicios = self.env['sale.order.line'].search([('order_id','=', self.project.venta_id.id)])

        # for i in servicios:
        #     print (i.product_id.id)


        # aqui sumo los totales de costo de los certificados anteriores menos el actual
        totales = []
        for k in servicios:
            suma = 0
            for i in listadecertificados:
                for j in i.detallecertificado_ids:
                    if (j.product_id.id == k.product_id.id):
                        suma = suma + k.price_unit
            totales.append(suma)
        print (totales)

        # aqui sumo los totales de actividad en unidades de los certificados anteriores menos el actual
        cantidades = []
        descripciondelbien = []
        unidaddemedida = []
        preciounitario = []
        idss = []
        for k in servicios:
            suma = 0
            for i in listadecertificados:
                for j in i.detallecertificado_ids:
                    if (j.product_id.id == k.product_id.id):
                        suma = suma + j.quantity
            cantidades.append(suma)
            descripciondelbien.append(k.product_id.name)
            unidaddemedida.append(k.product_uom.name)
            preciounitario.append(k.price_unit)
            idss.append(k.product_id.id)
        print ('cantidades totales de los anteriores en unidades')
        print (cantidades)
        print ('lista de descripciones de los anteriores')
        print (descripciondelbien)
        print ('lista de las unidades de medidas de los anteriores')
        print (unidaddemedida)
        print ('lista de precios unitario de los anteriores')
        print (preciounitario)
        print ('lista de los id de los anteriores')
        print (idss)

        # aqui preparo el vector con los totales de los anteriores cantidades por precio unitario
        v_pu_por_cant = []
        aaaa = 0
        for i in range(0,len(cantidades)):
            aaaa = cantidades[i]*preciounitario[i]
            v_pu_por_cant.append(aaaa)

        print ('####################################################################')

        print (v_pu_por_cant)

        print ('####################################################################')

        ######################### Certificado actual

        # aqui pongo en el vector elvectorp los id de los servicios del ultimo certificado papaaa
        vector_aux = []
        vector_aux2 = []
        for i in self.detallecertificado_ids:
            vector_aux.append(i.product_id.id)
            vector_aux2.append(i.product_id.id)

        # print ('jojo')
        for i in range(0, len(vector_aux)-1):
            for j in range(i+1, len(vector_aux)):
                if(vector_aux[i] == vector_aux[j]):
                    vector_aux2[j]=0
        # for i in vector_aux2:
        #     print (i)

        elvectorp = []
        for i in vector_aux2:
            if(i!=0):
                elvectorp.append(i)
        # print (elvectorp)
        # el vector elvectorp tiene los ids distintos el certificado actual

        cantidadesceractual = []
        descripciondelbienceractual = []
        for i in elvectorp:
            suma = 0
            for j in self.detallecertificado_ids:
                if (i == j.product_id.id):
                    suma = suma + j.quantity
            cantidadesceractual.append(suma)
        # preciosunitariosceractual = []
        for i in elvectorp:
            for j in self.detallecertificado_ids:
                if (i == j.product_id.id):
                    descripciondelbienceractual.append(j.product_id.name)
                    break

        print (elvectorp)
        print (cantidadesceractual)
        print (descripciondelbienceractual)
        # print (preciosunitariosceractual)



        # aqui lleno el vecto purete
        # vvvd=[]
        # for i in elvectorp:
        #     for j in self.detallecertificado_ids:
        #         if(i == j.product_id.id):
        #             vvvd.append(j.price_unit)

        ############################################ IMPORTANTE #######################################################################################3
        # aqui cargo el vector que se va a usar en el reporte
        # print ('cantidades totales de los anteriores en unidades')
        # print (cantidades)
        # print ('lista de descripciones de los anteriores')
        # print (descripciondelbien)
        # print ('lista de las unidades de medidas de los anteriores')
        # print (unidaddemedida)
        # print ('lista de precios unitario de los anteriores')
        # print (preciounitario)
        # print ('lista de los id de los anteriores')
        # print (idss)

        v01=[]
        v02=[]
        for i in range(0,len(idss)):
            v01.append(descripciondelbien[i])
            v01.append(unidaddemedida[i])
            v01.append(preciounitario[i])
            v01.append(cantidades[i])
            v01.append(v_pu_por_cant[i])
            v02.append(v01)
            v01 = []

        print (v02)






        a = {'saludo':'hola'
             }
        return v02

    def hola2(self):
        a = [1,2,3,4,5]
        b = [
            {'hola':'hola'},
            {'chau':'chau'},
        ]
        c = [[1,2,3],[4,5],[6,7,8]]
        return c

    def hola3(self):
        print('hola3')