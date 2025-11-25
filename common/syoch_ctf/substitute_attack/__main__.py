from .solver import Solver, EMPTY_MAP
from .charset import add_word_mapping, charmap_to_translate_table, is_all_translatable

# * ==================================
S = """
------------------------------------------------------------------------------
rtsmcvpn zdcd yn jthc auvm - acdqhdsrj_yn_r_tldc_uvoebv_ve75359v
-------------------------------------------------------------------------------
vudgdj ajtbtctlyprz wvcvovitl kvn pzd pzycb nts ta ajtbtc fvlutlyprz wvcvovitl,
v uvsb tksdc kduu wstks ys thc bynpcyrp ys zyn tks bvj, vsb npyuu cdodoedcdb
votsm hn tkysm pt zyn muttoj vsb pcvmyr bdvpz, kzyrz zvffdsdb pzycpdds jdvcn
vmt, vsb kzyrz y nzvuu bdnrcyed ys ypn fctfdc fuvrd. atc pzd fcdndsp y kyuu tsuj
nvj pzvp pzyn uvsbtksdcatc nt kd hndb pt rvuu zyo, vupzthmz zd zvcbuj nfdsp v bvj
ta zyn uyad ts zyn tks dnpvpdkvn v npcvsmd pjfd, jdp tsd fcdppj acdqhdspuj pt ed
odp kypz, v pjfd vexdrp vsb lyrythn vsb vp pzd nvod pyod ndsndudnn. ehp zd kvn
tsd ta pztnd ndsndudnn fdcntsn kzt vcd ldcj kduu rvfveud ta uttwysm vapdc pzdyc
ktcubuj vaavycn, vsb, vffvcdspuj, vapdc stpzysm dund. ajtbtc fvlutlyprz, atc
ysnpvsrd, edmvs kypz sdgp pt stpzysm; zyn dnpvpd kvn ta pzd novuudnp; zd cvs pt
bysd vp tpzdc ods'n pveudn, vsb avnpdsdb ts pzdo vn v ptvbj, jdp vp zyn bdvpz yp
vffdvcdb pzvp zd zvb v zhsbcdb pzthnvsb ctheudn ys zvcb rvnz. vp pzd nvod pyod,
zd kvn vuu zyn uyad tsd ta pzd otnp ndsndudnn, avspvnpyrvu aduutkn ys pzd kztud
bynpcyrp. y cdfdvp, yp kvn stp nphfybypjpzd ovxtcypj ta pzdnd avspvnpyrvu aduutkn
vcd nzcdkb vsb yspduuymdsp dsthmzehp xhnp ndsndudnnsdnn, vsb v fdrhuyvc svpytsvu
atco ta yp.
"""


def main():
    solver = Solver(S)
    initial_map = EMPTY_MAP
    initial_map = add_word_mapping(initial_map, "rtsmcvpn", "congrats", verbose=True)
    initial_map = add_word_mapping(initial_map, "pzd", "the", verbose=True)
    initial_map = add_word_mapping(initial_map, "zdcd", "here", verbose=True)
    initial_map = add_word_mapping(initial_map, "yn", "is", verbose=True)
    initial_map = add_word_mapping(initial_map, "jthc", "your", verbose=True)
    initial_map = add_word_mapping(initial_map, "auvm", "flag", verbose=True)
    initial_map = add_word_mapping(initial_map, "tldc", "over", verbose=True)
    initial_map = add_word_mapping(initial_map, "uvoebv", "lambda", verbose=True)
    initial_map = add_word_mapping(initial_map, "acdqhdsrj", "frequency", verbose=True)
    initial_map = add_word_mapping(
        initial_map, "vffvcdspuj", "apparently", verbose=True
    )
    decoded = solver.solve(initial_map=initial_map)

    s = set()
    for i, (charmap, text) in enumerate(decoded):
        if text in s:
            continue
        s.add(text)

        print(charmap)
        print(text)

        unmapped = solver.find_unmapped_word(charmap, max_length=1000)
        if unmapped is None:
            print("All words are mapped.")
        else:
            print(f"Unmapped word: {unmapped}")
            tab = charmap_to_translate_table(charmap)
            trans_tab = str.maketrans(tab)
            print("Translated text:")
            print(unmapped.translate(trans_tab))


def test():
    s = is_all_translatable("kypz", "fdrebp_u_y_vgsmtqcnola__ih")
    print(s)


if __name__ == "__main__":
    # test()
    main()
