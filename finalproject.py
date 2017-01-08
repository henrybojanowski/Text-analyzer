
from math import *


def clean_text(txt):
    """a helper function named clean_text(txt) that takes a string of text txt as a parameter and returns
a list containing the words in txt after it has been “cleaned”. This function will be used when you need to
process each word in a text individually, without having to worry about punctuation or special characters"""
    word=txt
    word=word.replace('.','')
    word=word.replace(',','')
    word=word.replace('?','')
    word=word.replace('/','')
    word=word.replace('(','')
    word=word.replace('!','')
    word=word.replace(')','')
    word=word.replace('"','')
    word=word.replace(';','')
    word=word.replace(':','')
    word = word.lower()
    list_of_split_words=txt.split()
    return list_of_split_words





def sample_file_write(filename, dictionary):
    """A function that demonstrates how to write a
       Python dictionary to an easily-readable file.
    """
    #d = {'test': 1, 'foo': 42}   # Create a sample dictionary.
    f = open(filename, 'w')      # Open file for writing.
    f.write(str(dictionary))              # Writes the dictionary to the file.
    f.close()                    # Close the file.



def sample_file_read(filename):
    """A function that demonstrates how to read a
       Python dictionary from a file.
    """
    f = open(filename, 'r')    # Open for reading.
    d_str = f.read()           # Read in a string that represents a dict.
    f.close()

    d = dict(eval(d_str))      # Convert the string to a dictionary.
    
def is_vowel_present(s):
    """helper function that determines if a vowel is present in a string if
this is true, return True, if False, return False"""
    if 'a' in s:
        return True
    elif 'i' in s:
        return True
    elif 'u' in s:
        return True
    elif 'e' in s:
        return True
    elif 'o' in s:
        return True
    else:
        return False

    
def stem(s):
    """parameter: string . The function should   then return the stem of s. The stem of a word
is the root part of the word, which excludes any prefixes and suffixes"""
    # is this a clean string or should I call that function
    # assume it's not for now
    # dictionary for special cases
    

    if s[-1]=='s':
        s=s[:-1]

    if s[-3:]=='ing': # ends in 'ing'
        #print('ends in "ing" executed')

        if len(s[-3:])< 4 and is_vowel_present(s[:-3])==False:
            #print('should not chop off the ing executed')
            return s
        
        elif s[-3]==s[-4]: # like stem and stemming i.e. 2 m's 
            return s[:-4]
            
        else: # no doubles
            return s[:-3]
              
    elif s[-2:]=='er':
        #print("er", 'executed')
        return s[:-2]
              
    elif s[-2:]=='ed':
        return s[:-2]

    elif s[-3:]=='ful':
        return s[:-3]
              
    elif s[:2]=='re':
        return s[2:]
    elif len(s)>4 and s[:4]=='homo':
        return s[4:]

##    elif s[-1]=='y':
##        s=s[:-1]
##        z=s+'i'
##        return z
    else:
        return s




def compare_dictionaries(d1,d2):
    """take two feature dictionaries d1 and d2 as inputs, and it should compute and return their
    log similarity score. Here is some pseudocode for what you will need to do"""

    sum_of_words_in_d1=0
    
    for key in d1:
        sum_of_words_in_d1+=d1[key]
    #print(sum_of_words_in_d1)
        
    score=0
    for key in d2:
        #print(key)
        if key in d1:
            #how_many_times_present=sum([1 for x in range(len(d1)) if x==value])
            # must think about how many occurences there are
            #print('is present is executed')
            
            score+=d2[key]*(log((d1[key])/(sum_of_words_in_d1)))
            #print(score)
        else:
            #print('is not present is executed')
            score+=d2[key]*(log((0.5)/(sum_of_words_in_d1)))
            #print(score)
    #print(score)        
    return score
            
    
class TextModel:


    def __init__(self, model_name):
        self.name=model_name
        self.words={} # records the number of times each word occurs in text
        self.word_lengths={} # like {1:23,2:76,3:98} # records the number of times
        # each word length appears
        self.stems={} # like spam for spamming
        self.sentence_lengths={} # number of words in a sentence
        self.rare_words={} # returns the rarest words in self.words and the
        # number of times they appear
        

    def __repr__(self):
        s=  'text model name: ' + self.name + '\n'
        s+= '   number of words: ' + str(len(self.words)) + '\n'
        s+= '   number of word lengths:' + str(len(self.word_lengths)) +'\n'
        s+= '   number of sentence lengths:' +str(len(self.sentence_lengths)) +'\n'
        s+= '   number of stems:' + str(len(self.stems)) +'\n'
        s+= '   number of rare words:' + str(len(self.rare_words))
        
                                    
        
        return s
                      
    def add_string(self,s):                                      
           """a method add_string(self, s) that adds a string of text s to the model by
    augmenting the feature dictionaries defined in the constructor. It should not
    explicitly return a value"""
           clean_word_list=clean_text(s)

           for word in clean_word_list:
               if word not in self.words: # new key and value in dict
                   self.words[word]=1
               else:  # increment the pre-existing key
                   self.words[word]+=1
            
           for word in clean_word_list:
               if len(word) not in self.word_lengths: # new key and value in dict
                   self.word_lengths[len(word)]=1
               else: # increment the pre-existing key
                   self.word_lengths[len(word)]+=1

        
           for word in clean_word_list:
               if stem(word) not in self.stems:
                   self.stems[stem(word)]=1
               else:
                   self.stems[stem(word)]+=1
                
           for key in self.words: # rare words
               if self.words[key]<3:
                   self.rare_words[key]=self.words[key]
            
        
            
                
           s= s.replace('.','!')
           s= s.replace('?','!')

           sentences=s.split('! ') # creates a list
           words_in_sentences=[]
           for index in range(len(sentences)): # creates a list of lists
               words_in_sentences+=[sentences[index].split(' ')]

           for lists in range(len(words_in_sentences)):
            
               if len(words_in_sentences[lists]) not in self.sentence_lengths:
                 self.sentence_lengths[len(words_in_sentences[lists])]=1
               else:
                 self.sentence_lengths[len(words_in_sentences[lists])]+=1
            
        

    def add_file(self,filename):
        f = open(filename, 'r', encoding='utf8', errors='ignore')
        read_in=f.read()
        f.close()
        self.add_string(read_in)

    def save_model(self):
        """a method save_model(self) that saves the TextModel object self by writing its
    various feature dictionaries to files. There will be one file written for each feature
    dictionary. For now, you just need to handle the words and word_lengths dictionaries"""
##        sample_file_write(filename, self.words) # for word dictionary
##        sample_file_read(filename)
##        print("Inside the newly-read dictionary","self.words" , "we have:")
##        print(d)
##        capital_letters_list=[x for x in self.name if x==x.upper()]
##        c=''
##        for index in range(len(capital_letters_list)):
##            c+=index
        
            
        filename=self.name+'_words.txt'
        print(filename)
        dictionary=self.words
        #print(self.words)
        f= open(filename, 'w')
        f.write(str(dictionary))
        f.close()

        filename1=self.name+'_word_lengths.txt'
        print(filename1)
        dictionary1=self.word_lengths
        f1=open(filename1,'w')
        f1.write(str(dictionary1))
        f1.close()

        filename2=self.name+'_sentence_lengths.txt'
        print(filename2)
        dictionary2=self.sentence_lengths
        f2=open(filename2,'w')
        f2.write(str(dictionary2))
        f2.close()

        filename3=self.name+ '_stems.txt'
        print(filename3)
        dictionary3=self.stems
        f3=open(filename3,'w')
        f3.write(str(dictionary3))
        f3.close()

        filename4=self.name+'_rare_words.txt'
        print(filename4)
        dictionary4=self.rare_words
        f4=open(filename4,'w')
        f4.write(str(dictionary4))
        f4.close()
        

    def read_model(self):
        """ a method read_model(self) that reads the stored dictionaries for the called TextModel
    object from their files and assigns them to the attributes of the called TextModel"""


        newfilename0=self.name+'_words.txt'
    
        f=open(newfilename0,'r')
        d_str=f.read()
        f.close()
        d=dict(eval(str(d_str)))
        print(d)
        self.words=d


        newfilename=self.name+'_word_lengths.txt'
    
        f1=open(newfilename, 'r')
        d_str1=f1.read()
        f1.close()
        d1=dict(eval(str(d_str1)))
        self.word_lengths=d1

        newfilename1=self.name+'_sentence_lengths.txt'
        
        f2=open(newfilename1, 'r')
        d_str2=f2.read()
        f2.close()
        d2=dict(eval(str(d_str2)))
        self.sentence_lengths=d2

        newfilename2=self.name+ '_stems.txt'

        f3=open(newfilename2, 'r')
        d_str3=f3.read()
        f3.close()
        d3=dict(eval(str(d_str3)))
        self.stems=d3

        newfilename3=self.name+'_rare_words.txt'
        
        f4=open(newfilename3, 'r')
        d_str4=f4.read()
        f4.close()
        d4=dict(eval(str(d_str4)))
        self.rare_words=d4

                  
    def similarity_scores(self,other):
        """a method similarity_scores(self, other) that computes
    and returns a list of log similarity scores measuring the similarity
    of self and other – one score for each type of feature (words, word lengths,
    stems, sentence lengths, and your additional feature). You should make repeated
    calls to compare_dictionaries, and put the resulting scores in a list that the
    method returns"""
        
        word_score = compare_dictionaries(other.words,self.words)
        word_lengths_score=compare_dictionaries(other.word_lengths,self.word_lengths)
        sentence_lengths_score=compare_dictionaries(other.sentence_lengths,self.sentence_lengths)
        stems_score=compare_dictionaries(other.stems,self.stems)
        rare_words_score=compare_dictionaries(other.rare_words,self.rare_words)
                  
        newlist=[word_score]+[word_lengths_score]+[sentence_lengths_score]+[stems_score]+[rare_words_score]
        newer_list=[]
        for x in range(len(newlist)):
            newer_list+=[round(newlist[x],3)]


        return newer_list
    
        
    def classify(self,source1,source2):
        """a method classify(self, source1, source2) that compares the called TextModel object (self) to two
    other “source” TextModel objects (source1 and source2) and determines which of these other TextModels is
    the more likely source of the called TextModel"""
        # inputs 2 TextModel objects
        # returns a statement on whi
        
        scores1=self.similarity_scores(source1)
        print('scores for', source1.name+':',scores1)
        scores2=self.similarity_scores(source2)
        print('scores for', source2.name+':',scores2)

        scores1_final=0
        scores2_final=0
        for x in range(len(scores1)):
            if scores1[x]>scores2[x]:
                scores1_final+=1
            else:
                scores2_final+=1

                
        if scores1_final>scores2_final:
            print(self.name+' '+'is more likely to have from '+source1.name )
        else:
            print(self.name+' '+'is more likely to have from '+source2.name )
        
        

def test():
    source1=TextModel('source1')
    source1.add_string('It is very interesting that she is interested')

    source2=TextModel('source2')
    source2.add_string('I am very, very excited about this!')
    
    mystery=TextModel('mystery')
    mystery.add_string('Is he interested? No, but I am.')
    mystery.classify(source1,source2)

    
    
def run_tests():
    """runs a bunch of text comparisons"""
    source1=TextModel('rowling')
    source1.add_file('rowling_source_text.txt')

    source2= TextModel('shakespeare')
    source2.add_file('shakespeare_source_text.txt')

    new1=TextModel('core_final_paper')# model
    new1.add_file('final_core_paper_source_text.txt')
    new1.classify(source1, source2)

    new2=TextModel('fy101')
    new2.add_file('fy101_source_text.txt')
    new2.classify(source1,source2)

    new3=TextModel('hs_essay')
    new3.add_file('hs_essay_source_text.txt')
    new3.classify(source1,source2)


    new4= TextModel('bu_app_essay')
    new4.add_file('bu_app_essay_source_text.txt')
    new4.classify(source1,source2)
    

                  
                  

                
            
                  

