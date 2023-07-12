rabinfos2 = [
        {
            #app_instance_id: Identificador exclusivo para a instância do aplicativo MEC.
            'app_instance_id' : 'kaique_01',
            # As informações sobre usuários por célula, conforme definido abaixo.
            'cell_user_info' : 
                        {
                            'ecgi' : 
                                {
                                    'cell_id' :
                                        {
                                            # cellid: String representando a Identidade da Célula E-UTRAN. Codificado como uma cadeia de bits (tamanho (28)) conforme definido em ETSI TS 136 413 [i.3].
                                            'cellid' : 'cell_02154',
                                            # nrcellid: String representando a Identidade da Célula NR. Codificado como uma cadeia de bits (tamanho (36)) conforme definido em ETSI TS 138 423 [i.17].
                                            'nrcellid' : 'nr_0287870'
                                        },
                                    'plmn' :{
                                        'plmn' : 
                                            {
                                                'mcc' : 'mcc',
                                                'mnc' : 'mnc'
                                            }
                                    }
                                   
                                },
                            # ue_info: Informações sobre UEs na célula específica conforme definido abaixo.
                            'ue_info':
                                {
                                    # 0 a N identificadores para associar o evento a um UE ou fluxo específico.
                                    'associate_id' : 
                                            {
                                                'Type': 'forte',
                                                'value': 'constante'
                                            },
                                    'erab_info' : 
                                            {
                                                'erab_id' : 1,
                                                'erab_qos_parameters' :
                                                            {
                                                                'qci' : 1,
                                                                'qos_information' : 
                                                                            {
                                                                                'erab_gbr_dl' : 1,
                                                                                'erab_gbr_ul' : 1,
                                                                                'erab_mbr_dl' : 1,
                                                                                'erab_mbr_ul' : 1
                                                                            }
                                                            }
                                            }
                                }
                        },
            #request_id: Identificador único atribuído pelo consumidor do serviço para o pedido de informação RAB
            'request_id' : 'doKaique',
            # time_stamp: Carimbo de hora
            'time_stamp' : 
                    {
                        'nano_seconds' : 12,
                        'seconds': 13
                    }
        }
]

