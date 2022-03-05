
'''
/**************************************************************
 *                                                            *
 *                     Done By: ApoAlquaary                   *
 *            Github: https://github.com/ApoAlquaary          *
 *                    Date: 23/10/2021                        *
 * 				   	 									      *
 *************************************************************/
'''

import random

class DNA:
    def __init__(self, target):
        self.fit_value = 0
        self.genes = []
        for i in range(len(target)):
            self.genes.append(chr(random.choice(range(32, 123))))

    def update_fitness(self, target):
        score = 0
        for i in range(len(target)):
            if(self.genes[i] == target[i]):
                score += 1
        self.fit_value = float(score) / float(len(target))

    def cross_over(self, partner):
        child = DNA((self.genes))
        mid_point = random.randint(0, len(self.genes) - 1)
        child.genes[0: mid_point] = partner.genes[0: mid_point]
        child.genes[mid_point: len(self.genes)] = self.genes[mid_point: len(self.genes)]
        return child

    def mutation(self, mu_ratio):

        for i in range(len(self.genes)):
            if(random.random() < mu_ratio):
                self.genes[i] = chr((random.choice(range(32, 123))))


    def get_sentance(self):
        return ''.join(self.genes)
