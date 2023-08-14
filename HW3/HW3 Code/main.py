from pyrouge import Rouge155
import time


def print_result(type):
    print('Rouge_' + type)
    print('Recall', round(output_dict['rouge_' + type + '_recall'] * 100, 2))
    print('Precision', round(output_dict['rouge_' + type + '_precision'] * 100, 2))
    print('F_score', round(output_dict['rouge_' + type + '_f_score'] * 100, 2))


name_list = ['Centroid', 'DPP', 'ICSISumm', 'LexRank', 'Submodular']
for i in name_list:
    start = time.time()
    r = Rouge155()
    r.system_dir = 'System_Summaries/' + i
    r.model_dir = 'Human_Summaries/eval'
    r.system_filename_pattern = 'd(\d+)*t\\.' + i
    r.model_filename_pattern = 'D#ID#\\.M\\.100\\.T\\.[A-Z]'

    output = r.convert_and_evaluate()
    output_dict = r.output_to_dict(output)
    end = time.time()
    print(i)
    print(end-start)
    # print_result('1')
    # print_result('2')
    # print_result('l')
