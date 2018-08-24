class AgreementTemplate():
    def __init__(self):
        self.rules = {'obj_rel_anim': (['D', 'MS', 'C', 'D', 'ES', 'EV', 'MV'], [{'match':([1],[6]), 'vary':[4,5]}, {'match':([4],[5]), 'vary':[1,6]}]),
                      'obj_rel_inanim': (['D', 'IS', 'IC', 'D', 'ES', 'EV', 'IV'], [{'match': ([1],[6]), 'vary':[4,5]}, {'match': ([4],[5]), 'vary':[1,6]}]),
                      'subj_rel': (['D', 'MS', 'C', 'EV', 'D', 'ES', 'MV'], [{'match':([1,3],[6]), 'vary': [5]}]),
                      'prep_anim': (['D', 'MS', 'P', 'D', 'ES', 'MV'], [{'match':([1],[5]), 'vary':[4]}]),
                      'prep_inanim': (['D', 'IS', 'IP', 'D', 'ES', 'IV'], [{'match':([1],[5]), 'vary':[4]}]),
                      'obj_rel_no_comp': (['D', 'MS', 'D', 'ES', 'EV', 'MV'], [{'match':([1],[5]), 'vary':[3,4]}, {'match':([3],[4]), 'vary':[1,5]}]),
                      'obj_rel_no_comp_inanim': (['D', 'IS', 'D', 'ES', 'EV', 'IV'], [{'match':([1],[5]), 'vary':[3,4]}, {'match':([3],[4]), 'vary':[1,5]}]),
                      'simple_agrmt': (['D', 'MS', 'MV'], [{'match':([1],[2]), 'vary':[]}]),
                      'stmt_before_sent': (['D', 'BS', 'BV', 'D', 'MS', 'MV'], [{'match':([4],[5]), 'vary':[1]}]),
                      'vp_coord': (['D', 'MS', 'MV', 'AND', 'MV'], [{'match':([1,2],[4]), 'vary':[]}]),
                      'long_vp_coord': (['D', 'MS', 'LMV', 'AND', 'LMV'], [{'match':([1,2],[4]), 'vary':[]}]),
                      'reflexives': (['D', 'MS', 'C', 'D', 'ES', 'EV', 'RMV', 'ANPHR'], [{'match':([1], [7]), 'vary':[4,5]}]),
                      'simple_reflexives':(['D', 'MS', 'RMV', 'ANPHR'], [{'match':([1],[3]), 'vary':[]}]),
                      'stmt_before_reflexive':(['D', 'BS', 'BV', 'D', 'MS', 'RMV', 'ANPHR'], [{'match':([4],[6]), 'vary':[1]}])}

        # TO CREATE NEW CONSTRUCTIONS, PLEASE FOLLOW THIS FORMAT:
        # 'name': ([list of preterminals], [list of dicts containing ('match', 'vary') indices formatted as below])
        # [{'match':([first indices (subject)], [second indices (verb/anaphor)]), 'vary':[list of indices for words to vary in number (attractors)]},
        #  {additional dicts if there are multiple constructions to examine, e.g. (1) main subject-verb mismatch; (2) embedded subject-verb mismatch}]

class NPITemplate():
    def __init__(self):
        self.rules = {'npi_anim': (['NO', 'MS', 'C', 'D', 'ES', 'EV', 'PASTAUX', 'NPI', 'APMV'], None), 
                      'npi_inanim': (['NO', 'IS', 'C', 'D', 'ES', 'EV', 'PASTAUX', 'NPI', 'IPMV'], None),
                      'simple_npi_anim': (['NO', 'MS', 'PASTAUX', 'NPI', 'APMV'], None),
                      'simple_npi_inanim': (['NO', 'IS', 'PASTAUX', 'NPI', 'IPMV'], None)}
        # TO CREATE NEW CONSTRUCTIONS, PLEASE FOLLOW THIS FORMAT:
        # 'name': ([list of preterminals], None)
        # For NPIs, we aren't looking at sentences that are minimally different so the 'match/vary' schema in the AgreementTemplate doesn't work here