from models.periodo import Periodo

class Calculadora:
    @staticmethod
    def reporte(valor_inicial, valor_final, periodos):
        cont = 0
        calculo = Calculadora.alemana(periodos)
        reporte_data = []
        while cont < len(calculo):
            if calculo[cont][1] >= valor_inicial and calculo[cont][1] <= valor_final:
                reporte_data.append(calculo[cont])
            cont += 1
        return reporte_data

    @staticmethod
    def alemana(prestamo):
        cont = 0
        saldo_anterior = 0.0
        while cont < len(prestamo.get_periodos()):
            aux = []
            p = Periodo(cont + 1)
            p.set_abono_capital(round(prestamo.get_monto()/prestamo.get_plazo(),2))
            if cont == 0:
                p.set_capital_inicio(round(prestamo.get_monto(),2))
            else:
                p.set_capital_inicio(round(saldo_anterior,2))
            p.set_interes(round(((prestamo.get_interes()/12)/100)*p.get_capital_inicio(),2))
            p.set_cuota(round(p.get_interes()+p.get_abono_capital(),2))
            p.set_saldo(round(p.get_capital_inicio()-p.get_abono_capital(),2))
            saldo_anterior = p.get_saldo()
            aux.append(p.get_cantidad())
            aux.append(p.get_cuota())
            aux.append(p.get_capital_inicio())
            aux.append(p.get_interes())
            aux.append(p.get_abono_capital())
            aux.append(p.get_saldo())
            prestamo.get_periodos()[cont] = aux
            cont += 1
        return prestamo.get_periodos() 