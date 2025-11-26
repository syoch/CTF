from syoch_ctf.data_processor.charmap import CharMap
from syoch_ctf.crypto.substitute_solver import SubstituteSolver as Solver


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
    initial_map = CharMap()
    initial_map.add_word_mapping("rtsmcvpn", "congrats", verbose=True)
    initial_map.add_word_mapping("pzd", "the", verbose=True)
    initial_map.add_word_mapping("zdcd", "here", verbose=True)
    initial_map.add_word_mapping("yn", "is", verbose=True)
    initial_map.add_word_mapping("jthc", "your", verbose=True)
    initial_map.add_word_mapping("auvm", "flag", verbose=True)
    initial_map.add_word_mapping("tldc", "over", verbose=True)
    initial_map.add_word_mapping("uvoebv", "lambda", verbose=True)
    initial_map.add_word_mapping("acdqhdsrj", "frequency", verbose=True)
    initial_map.add_word_mapping("vffvcdspuj", "apparently", verbose=True)
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
            print("Translated text:")
            print(charmap.translate_text(unmapped))


if __name__ == "__main__":
    main()
