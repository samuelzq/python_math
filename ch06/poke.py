# -*- coding: utf-8 -*-
"""
对一副扑克牌进行描述，并模拟发牌。
"""

class Card:
    """
    一张扑克牌
    
    ...
    属性
    ____
    rank: string
        牌的大小
    suit: string
        牌的花色
    order: int
        一张牌在牌堆的顺序
    is_dace_up: bool
        牌面是否向上
    
    方法
    ____
    pic_order:
        返回牌在牌堆中的序号
    """
    RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
    SUITS = ('梅花', '方片', '红桃', '黑桃')

    def __init__(self, rank, suit, face_up=True):
        self.rank = rank              # 牌面数字1~13
        self.suit = suit              # 花色
        self.order = self.pic_order()
        self.is_face_up = face_up     # 是否显示牌的正面，True为正面，False为反面

    def __str__(self):
        """ 打印一张牌的信息 """
        if self.is_face_up:
            rep = self.suit + self.rank
        else:
            rep = 'XX'
        return rep

    def pic_order(self):
        """ 牌的顺序号 """
        if self.rank == 'A':
            face_num = 1
        elif self.rank == 'J':
            face_num = 11
        elif self.rank == 'Q':
            face_num = 12
        elif self.rank == 'K':
            face_num = 13
        else:
            face_num = int(self.rank)
        if self.suit == '梅花':
            suit = 1
        elif self.suit == '方片':
            suit = 2
        elif self.suit == '红桃':
            suit = 3
        else:
            suit = 4
        return (suit - 1) * 13 + face_num
    
class Cards:
    """
    一些牌
    
    ...
    属性
    ____
    cards: list
        一副扑克牌
    
    方法
    ____
    shuffle:
        洗牌
    sort:
        理牌
    add:
        抓牌
    """

    def __init__(self):
        self.cards = []     # cards列表变量用来存储牌

    def __del__(self):
        del self.cards
        
    def __str__(self):
        """ 将所有的牌显示出来 """
        if self.cards:
            rep = ''
            for card in self.cards:
                rep += str(card) + '\t'
        else:
            rep = '无牌'
        return rep
        
    def shuffle(self):
        """ 洗牌 """
        import random
        random.shuffle(self.cards)
    
    def sort(self):
        """ 理牌 """
        self.cards.sort(key=Card.pic_order)
    
    def add(self, card):
        """ 抓牌 """
        self.cards.append(card)

class Hand(Cards):
    """ 玩家的一手牌 """

    def __init__(self):
        super(Hand, self).__init__()
        pass

class Poke(Cards):
    """
    Poke类代表一副52张的牌，继承Cards类。
    增加抓牌方法
    """

    def __init__(self):
        """ 生成一副牌 """
        super(Poke, self).__init__()
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))
     
    def get(self):
        """ 抓牌 """
        if (len(self.cards)):
            return self.cards.pop()
        else:
            print("牌发完了")
            return None

if __name__ == '__main__':
    import math
    players = [Hand(), Hand(), Hand(), Hand(), Hand()]
    poke = Poke()   # 生成一副牌
    poke.shuffle()  # 洗牌
    per_hand = math.ceil(52 / len(players))
    
    """
    抓牌
    每轮每个玩家依次抓一张
    """
    for round in range(per_hand):
        for hand in players:
            card = poke.get();
            if (card != None):
                hand.add(card)
            else:
                break

    n = 1
    for hand in players:
        print('牌手', n, end=':')
        hand.sort()
        print(hand)
        n = n + 1