import csv, os


class Apriori:

    def __init__(self, minsupport):
        self.minsupport = minsupport
        self.buckets = []
        with open(os.path.join(__file__, "../", "buckets_new.csv"), 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                self.buckets.append(row)

    def get_disease(self, symptomlist, buckets):
        disease_score = {}
        score = 0
        for bucket in buckets:
            print(bucket)
            score = set(symptomlist) & set(bucket)
            score = float(len(score)) / float(len(symptomlist)) * 100
            print(score)
            if score > 0:
                disease = self.get_disease_given_bucket(bucket)
                print(disease)
                disease_score[disease] = score
        result = ''
        result += 'Disease - Probability scores\n'

        with open(os.path.join(__file__, "../", "disease_probabilityscores_from_symptomlist.csv"), "wt",
                  encoding='utf-8', newline='') as csvfile:
            writer = csv.writer(csvfile)

            writer.writerow(["Symptomlist"])
            writer.writerow(symptomlist)
            writer.writerow(["Disease", "Probability scores"])
            for key, value in disease_score.items():
                writer.writerow([key, value])
                print([key, value])

        print(result)
        return result

    def get_disease_given_bucket(self, bucket):
        disease = ""
        print("ENTER")
        with open(os.path.join(__file__, "../", "rollup_dataset.csv"), 'rt', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                row_clean = [i for i in row if i]
                bucket_clean = [i for i in bucket if i]
                if len(row_clean) == (len(bucket_clean) + 1):
                    if all(values in row_clean for values in bucket_clean):
                        disease = row_clean[0]
                        break

        return disease

    def Apriori_gen(self, Itemset, lenght):
        """Too generate new (k+1)-itemsets can see README Join Stage"""
        canditate = []
        canditate_index = 0
        for i in range(0, lenght):
            element = str(Itemset[i])
            for j in range(i + 1, lenght):
                element1 = str(Itemset[j])
                if element[0:(len(element) - 1)] == element1[0:(len(element1) - 1)]:
                    unionset = element[0:(len(element) - 1)] + element1[len(element1) - 1] + element[
                        len(element) - 1]  # Combine (k-1)-Itemset to k-Itemset
                    unionset = ''.join(sorted(unionset))  # Sort itemset by dict order
                    canditate.append(unionset)
        return canditate

    def Apriori_prune(self, Ck, minsupport):
        L = []
        for i in Ck:
            if Ck[i] >= minsupport:
                L.append(i)
        return sorted(L)

    def Apriori_count_subset(self, Canditate, Canditate_len):

        """ Use bool to know is subset or not """
        Lk = dict()
        for l in self.buckets:
            l = str(l.split(","))
            for i in range(0, Canditate_len):
                key = str(Canditate[i])
                if key not in Lk:
                    Lk[key] = 0
                flag = True
                for k in key:
                    if k not in l:
                        flag = False
                if flag:
                    Lk[key] += 1
        return Lk

    def apriori(self):
        C1 = {}
        for line in self.buckets:
            new_line = ','.join(line)
            for item in new_line.split(','):
                if item in C1:
                    C1[item] += 1
                else:
                    C1[item] = 1
        sorted(C1.keys())
        L1 = self.Apriori_prune(C1, self.minsupport)
        L = self.Apriori_gen(L1, len(L1))
        print('====================================')
        print('Frequent 1-itemset is', L1)
        print('====================================')

        k = 2
        while L != []:
            C = self.Apriori_count_subset(L, len(L))
            frequent_itemset = self.Apriori_prune(C, self.minsupport)
            print('====================================')
            print('Frequent', k, '-itemset is', frequent_itemset)
            print('====================================')
            L = self.Apriori_gen(frequent_itemset, len(frequent_itemset))
            k += 1

        return self.get_disease(L1, self.buckets)


ap = Apriori(2)
ap.apriori()