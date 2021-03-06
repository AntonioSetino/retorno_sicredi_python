# -*- coding: UTF-8 -*-

from string_utils import is_full_string

class Subocorrencias(object):

    @staticmethod
    def retornar(ocorrencia, subocorrencias):

        map_subocorrencias_28 = {'03':'Tarifa de sustacao', '04':'Tarifa de protesto', '08':'Tarifa de custos de protesto', 
        'A9':'Tarifa de manutencao de titulo vencido', 'B1':'Tarifa de baixa da carteira', 
        'B3':'Tarifa de registro de entrada do titulo', 'F5':'Tarifa de entrada na rede Sicredi'}

        map_subocorrencias = {'01':'Código do banco inválido',
            '02':'Código do registro detalhe inválido',
            '03':'Código da ocorrência inválido',
            '04':'Código de ocorrência não permitida para a carteira',
            '05':'Código de ocorrência não numérico',
            '07':'Cooperativa/agência/conta/dígito inválidos',
            '08':'Nosso número inválido',
            '09':'Nosso número duplicado',
            '10':'Carteira inválida',
            '14':'Título protestado',
            '15':'Cooperativa/carteira/agência/conta/nosso número inválidos',
            '16':'Data de vencimento inválida',
            '17':'Data de vencimento anterior à data de emissão',
            '18':'Vencimento fora do prazo de operação',
            '20':'Valor do título inválido',
            '21':'Espécie do título inválida',
            '22':'Espécie não permitida para a carteira',
            '24':'Data de emissão inválida',
            '29':'Valor do desconto maior/igual ao valor do título',
            '31':'Concessão de desconto - existe desconto anterior',
            '33':'Valor do abatimento inválido',
            '34':'Valor do abatimento maior/igual ao valor do título',
            '36':'Concessão de abatimento - existe abatimento anterior',
            '38':'Prazo para protesto inválido',
            '39':'Pedido para protesto não permitido para o título',
            '40':'Título com ordem de protesto emitida',
            '41':'Pedido cancelamento/sustação sem instrução de protesto',
            '44':'Cooperativa de crédito/agência beneficiária não prevista',
            '45':'Nome do pagador inválido',
            '46':'Tipo/número de inscrição do pagador inválidos',
            '47':'Endereço do pagador não informado',
            '48':'CEP irregular',
            '49':'Número de Inscrição do pagador/avalista inválido',
            '50':'Pagador/avalista não informado',
            '60':'Movimento para título não cadastrado',
            '63':'Entrada para título já cadastrado',
            'A':'Aceito',
            'D':'Desprezado',
            'A1':'Praça do pagador não cadastrada.',
            'A2':'Tipo de cobrança do título divergente com a praça do pagador.',
            'A3':'Cooperativa/agência depositária divergente: atualiza o cadastro de praças da Coop./agência beneficiária',
            'A4':'Beneficiário não cadastrado ou possui CGC/CIC inválido',
            'A5':'Pagador não cadastrado',
            'A6':'Data da instrução/ocorrência inválida',
            'A7':'Ocorrência não pode ser comandada',
            'A8':'Recebimento da liquidação fora da rede Sicredi - via compensação eletrônica',
            'B4':'Tipo de moeda inválido',
            'B5':'Tipo de desconto/juros inválido',
            'B6':'Mensagem padrão não cadastrada',
            'B7':'Seu número inválido',
            'B8':'Percentual de multa inválido',
            'B9':'Valor ou percentual de juros inválido',
            'C1':'Data limite para concessão de desconto inválida',
            'C2':'Aceite do título inválido',
            'C3':'Campo alterado na instrução “31 – alteração de outros dados” inválido',
            'C4':'Título ainda não foi confirmado pela centralizadora',
            'C5':'Título rejeitado pela centralizadora',
            'C6':'Título já liquidado',
            'C7':'Título já baixado',
            'C8':'Existe mesma instrução pendente de confirmação para este título',
            'C9':'Instrução prévia de concessão de abatimento não existe ou não confirmada',
            'D1':'Título dentro do prazo de vencimento (em dia)',
            'D2':'Espécie de documento não permite protesto de título',
            'D3':'Título possui instrução de baixa pendente de confirmação',
            'D4':'Quantidade de mensagens padrão excede o limite permitido',
            'D5':'Quantidade inválida no pedido de boletos pré-impressos da cobrança sem registro',
            'D6':'Tipo de impressão inválida para cobrança sem registro',
            'D7':'Cidade ou Estado do pagador não informado',
            'D8':'Seqüência para composição do nosso número do ano atual esgotada',
            'D9':'Registro mensagem para título não cadastrado',
            'E2':'Registro complementar ao cadastro do título da cobrança com e sem registro não cadastrado',
            'E3':'Tipo de postagem inválido, diferente de S, N e branco',
            'E4':'Pedido de boletos pré-impressos',
            'E5':'Confirmação/rejeição para pedidos de boletos não cadastrado',
            'E6':'Pagador/avalista não cadastrado',
            'E7':'Informação para atualização do valor do título para protesto inválido',
            'E8':'Tipo de impressão inválido, diferente de A, B e branco',
            'E9':'Código do pagador do título divergente com o código da cooperativa de crédito',
            'F1':'Liquidado no sistema do cliente',
            'F2':'Baixado no sistema do cliente',
            'F3':'Instrução inválida, este título está caucionado/descontado',
            'F4':'Instrução fixa com caracteres inválidos',
            'F6':'Nosso número / número da parcela fora de seqüência – total de parcelas inválido',
            'F7':'Falta de comprovante de prestação de serviço',
            'F8':'Nome do beneficiário incompleto / incorreto.',
            'F9':'CNPJ / CPF incompatível com o nome do pagador / Sacador Avalista',
            'G1':'CNPJ / CPF do pagador Incompatível com a espécie',
            'G2':'Título aceito: sem a assinatura do pagador',
            'G3':'Título aceito: rasurado ou rasgado',
            'G4':'Título aceito: falta título (cooperativa/ag. beneficiária deverá enviá-lo)',
            'G5':'Praça de pagamento incompatível com o endereço',
            'G6':'Título aceito: sem endosso ou beneficiário irregular',
            'G7':'Título aceito: valor por extenso diferente do valor numérico',
            'G8':'Saldo maior que o valor do título',
            'G9':'Tipo de endosso inválido',
            'H1':'Nome do pagador incompleto / Incorreto',
            'H2':'Sustação judicial',
            'H3':'Pagador não encontrado',
            'H4':'Alteração de carteira',
            'H5':'Recebimento de liquidação fora da rede Sicredi – VLB Inferior – Via Compensação',
            'H6':'Recebimento de liquidação fora da rede Sicredi – VLB Superior – Via Compensação',
            'H7':'Espécie de documento necessita beneficiário ou avalista PJ',
            'H8':'Recebimento de liquidação fora da rede Sicredi – Contingência Via Compe',
            'H9':'Dados do título não conferem com disquete',
            'I1':'Pagador e Sacador Avalista são a mesma pessoa',
            'I2':'Aguardar um dia útil após o vencimento para protestar',
            'I3':'Data do vencimento rasurada',
            'I4':'Vencimento – extenso não confere com número',
            'I5':'Falta data de vencimento no título',
            'I6':'DM/DMI sem comprovante autenticado ou declaração',
            'I7':'Comprovante ilegível para conferência e microfilmagem',
            'I8':'Nome solicitado não confere com emitente ou pagador',
            'I9':'Confirmar se são 2 emitentes. Se sim, indicar os dados dos 2',
            'J1':'Endereço do pagador igual ao do pagador ou do portador',
            'J2':'Endereço do apresentante incompleto ou não informado',
            'J3':'Rua/número inexistente no endereço',
            'J4':'Falta endosso do favorecido para o apresentante',
            'J5':'Data da emissão rasurada',
            'J6':'Falta assinatura do pagador no título',
            'J7':'Nome do apresentante não informado/incompleto/incorreto',
            'J8':'Erro de preenchimento do titulo',
            'J9':'Título com direito de regresso vencido',
            'K1':'Título apresentado em duplicidade',
            'K2':'Título já protestado',
            'K3':'Letra de cambio vencida – falta aceite do pagador',
            'K4':'Falta declaração de saldo assinada no título',
            'K5':'Contrato de câmbio – Falta conta gráfica',
            'K6':'Ausência do documento físico',
            'K7':'Pagador falecido',
            'K8':'Pagador apresentou quitação do título',
            'K9':'Título de outra jurisdição territorial',
            'L1':'Título com emissão anterior a concordata do pagador',
            'L2':'Pagador consta na lista de falência',
            'L3':'Apresentante não aceita publicação de edital',
            'L4':'Dados do Pagador em Branco ou inválido',
            'L5':'Código do Pagador na agência beneficiária está duplicado',
            'M1':'Reconhecimento da dívida pelo pagador',
            'M2':'Não reconhecimento da dívida pelo pagador',
            'M3':'Inclusão de desconto 2 e desconto 3 inválido',
            'X1':'Regularização centralizadora – Rede Sicredi',
            'X2':'Regularização centralizadora – Compensação',
            'X3':'Regularização centralizadora – Banco correspondente',
            'X4':'Regularização centralizadora - VLB Inferior - via compensação',
            'X5':'Regularização centralizadora - VLB Superior - via compensação',
            'X0':'Pago com cheque',
            'X6':'Pago com cheque – bloqueado 24 horas',
            'X7':'Pago com cheque – bloqueado 48 horas',
            'X8':'Pago com cheque – bloqueado 72 horas',
            'X9':'Pago com cheque – bloqueado 96 horas',
            'XA':'Pago com cheque – bloqueado 120 horas',
            'XB':'Pago com cheque – bloqueado 144 horas'}

        set_subocorrencias = {'-'}
        if is_full_string(subocorrencias):
            for i in range(0, len(subocorrencias)):
                if i % 2 == 0:
                    subocorrencia = subocorrencias[i:i+2]
                    if subocorrencia != '00':
                        if ocorrencia == '28':
                            set_subocorrencias.add(map_subocorrencias_28.get(subocorrencia))
                        else:
                            set_subocorrencias.add(map_subocorrencias.get(subocorrencia))
        set_subocorrencias.remove('-')

        return list(set_subocorrencias)