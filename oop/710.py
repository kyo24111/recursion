def complement(x):
    return not x

def assertDemorgan(p,q):
    # ~(p ∧ q) ≡ ~p v ~q
    assert(complement(p and q) == (complement(p) or complement(q)))

    # ~(p v q) ≡ ~p ∧ ~q
    assert(complement(p or q) == (complement(p) and complement(q)))

# ドモルガンの法則が成立するかチェック
# エラーは発生しない
assertDemorgan(True, True)
assertDemorgan(True, False)
assertDemorgan(False, True)
assertDemorgan(False, False)

class User:
    def __init__(self, name, numberID, isPaidUser):
        self.name = name
        self.numberID = numberID
        self.isPaidUser = isPaidUser
    
    # idが奇数の無料ユーザー以外にメールを送った
    # !(id % 2 == 1 and !isPaidUser) -> true
    # ドモルガンの法則を使って、複雑なロジックを書き換えます。
    def receiveEmail(self):
        
        isFreeUser = not self.isPaidUser
        # 可読性の上昇
        return self.numberID % 2 == 0 or isFreeUser
    
steve = User("steve", 200, True)
mike = User("mike", 201, True)
mary = User("mary", 202, False)
lisa = User("lisa", 203, False)

print(steve.receiveEmail())
print(mike.receiveEmail())
print(mary.receiveEmail())
print(lisa.receiveEmail())