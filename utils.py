class Utils(object):

    @staticmethod
    def formatar_data_json(data):
        if data is not None:
            vetor_data = data.split('T')[0].split('-')
            return '{}-{}-{} 00:00:00'.format(vetor_data[2], vetor_data[1], vetor_data[0])
        else:
            return None
