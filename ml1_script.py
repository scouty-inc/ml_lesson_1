# -*- coding: utf-8 -*-

from janome.tokenizer import Tokenizer
from nltk.probability import LidstoneProbDist

# バージョンアップによりnltk からNgramModelが削除されてしまったので、
# NgramModelの部分だけ抽出したnltkxライブラリをファイル内に入れて読み込む
from nltkx import NgramModel

NEWLINE = "\n"

def open_corpus(corpus_path):
    """
    corpus_path(str) に指定されたファイルを開き、改行を消してひとつの文字列(str)にして返す
    """

    pass


def tokenize(text):
    """
    日本語の text(str)を受け取って、単語ごとに切って、strのリストにして返す

    >>> tekenize("吾輩は猫である") -> ['吾輩', 'は', '猫', 'で', 'ある']
    """

    # ヒント
    # janomeの使い方は、http://mocobeta.github.io/janome/ 参照。
    # http://mocobeta.github.io/janome/api/janome.html#janome.tokenizer.Token も要チェック。

    pass


def train_model(corpus_path, n=2):
    """
    corpus_path(str)に指定されたファイルのテキストから言語モデルを学習し、n-gramで学習してモデルオブジェクトを返す
    """

    estimator = lambda fdist, bins: LidstoneProbDist(fdist, 0.2)

    # ヒント
    # >>> model = NgramModel(n, words, estimator)
    # で、NgramModelオブジェクトが学習＆生成される。
    # words(list of str) は訓練データとなる文を、単語ごとに切ったもの。
    # estimatorは、Smoothing(平滑化)といって、1度も出ていない単語の出現確率を他の単語から推定する手法のための推定器で、ここではおまじないと考えて良い

    return model


def per_word_cross_entropy(model, text):
    """
    model(NgramModel)とtext(str)をとり、modelにおけるtextのper-word クロスエントロピー(float)を返す
    """

    # ヒント
    # >>> model.entropy(words)
    # で words(list of str) で構成されるテキストの文全体のエントロピーが出せるので、これを文の単語数で割れば良い

    pass


def get_average_entropy(model, corpus_path, max_lines_to_load=-1):
    """
    corpus_path(str)に指定したファイルの冒頭 max_lines_to_load(int) 行の文の言語モデルオブジェクト model(NgramModel)
    で計ったクロスエントロピーの平均値を返す。
    例）max_lines_to_load = 30 の場合、冒頭30行の平均 per-word クロスエントロピーを返す
    """

    pass


def is_same_author(model_corpus_path, target_corpus_path, n=2, threshold=5.0):
    """
    target_corpus_path(str)に指定されたファイルの文章が、model_corpus_path(str)の著者のものだと推定されればTrueを返す
    thresholdは、その著者と判定するためのエントロピーの閾値
    nは、モデルのgram数
    """

    pass


if __name__ == "__main__":

    def test_get_average_entropy():
        n = 4
        max_lines_to_load = 60

        # 宮沢賢治 銀河鉄道の夜を学習して言語モデルをつくる
        model = train_model("./corpus/kenji_ginga.txt", n)

        # 各小説の平均エントロピーをprintする
        print("宮沢賢治 / 注文の多い料理店: {0}".format(get_average_entropy(model, "./corpus/kenji_ryoriten.txt", max_lines_to_load)))
        print("宮沢賢治 / 風の又三郎: {0}".format(get_average_entropy(model, "./corpus/kenji_matasaburo.txt", max_lines_to_load)))
        print("宮沢賢治 / ツェねずみ: {0}".format(get_average_entropy(model, "./corpus/kenji_tsuenezumi.txt", max_lines_to_load)))
        print("太宰治 / 走れメロス: {0}".format(get_average_entropy(model, "./corpus/dazai_melos.txt", max_lines_to_load)))
        print("森鴎外 / あそび: {0}".format(get_average_entropy(model, "./corpus/ogai_asobi.txt", max_lines_to_load)))
        print("夏目漱石 / こころ: {0}".format(get_average_entropy(model, "./corpus/soseki_kokoro.txt", max_lines_to_load)))
        print("夏目漱石 / 道草: {0}".format(get_average_entropy(model, "./corpus/soseki_michikusa.txt", max_lines_to_load)))


    def test_is_same_author():
        n = 4
        threshold = 5.0

        # 「銀河鉄道の夜」と「注文の多い料理店」の著者は同じか？
        print(is_same_author("./corpus/kenji_ginga.txt", "./corpus/kenji_ryoriten.txt", n, threshold))

        # 「銀河鉄道の夜」と「あそび」の著者は同じか？
        print(is_same_author("./corpus/kenji_ginga.txt", "./corpus/ogai_asobi.txt", n, threshold))


    # test_get_average_entropy()
    # test_is_same_author()
