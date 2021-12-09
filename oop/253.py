# メモ化は、ツリー構造が上から下へと続くアルゴリズムでのキャッシングです。
# フィボナッチのツリーを見てみると、nから始まり、n-1、n-2、n-3と下に向かって計算していきます。
def memoizationFib(totalFibNumbers):
    # これはキャッシュであり，すでに計算したフィボナッチ数をすべて保存します。全てをNoneに設定してください。
    cache = [None] * (totalFibNumbers+1)
    # キャッシュを更新するには、このローカルスコープ内の関数を使用します。
    def innerMemoizationFib(n):
        # キャッシュされていないフィボナッチ数を処理するだけです。
        # フィボナッチのnを再帰的に計算し，キャッシュに追加します．
        if cache[n] is None:
            if n == 0:
                cache[n] = 0
            elif n == 1:
                cache[n] = 1
            else:
                cache[n] = innerMemoizationFib(n - 1) + innerMemoizationFib(n - 2)

        # フィボナッチはすでに計算されているのでただ返すだけで問題ありません。
        return cache[n]
    return innerMemoizationFib(totalFibNumbers)

print(memoizationFib(50))