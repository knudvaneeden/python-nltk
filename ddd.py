import nltk

from nltk.book import *

print( "===" )
print( "text1 = ", text1 )
print( "===" )
print( "text2 = ", text2 )
print( "===" )
print( "concordance = ", text1.concordance("monstrous") )
print( "===" )
print( "similar = ", text1.similar("monstrous") )
print( "===" )
print( "similar = ", text2.similar("monstrous") )
print( "===" )
print( "very = ", text2.common_contexts( ["monstrous", "very"] ) )
print( "===" )
print ( "dispersian_plot (close the dialog box to continue) =" )
text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])
print( "===" )
#
# not available in Python version 3.x
#
# print ( "generate =" )
# text3.generate()
print( "===" )
print( "len( text( 3 ) ) = ", len( text3 ) )
print( "===" )
print( "sorted( set( text3 ) ) = ", sorted( set( text3 ) ) )
print( "===" )
print( "len(set(text3)) / len(text3)", len( set( text3 ) ) / len( text3 ) )
print( "===" )
print( "text3.count('smote') = ", text3.count( "smote" ) )
print( "===" )
print( " def lexical_diversity(text):" )
print( "  return len( set( text ) ) / len( text )" )
print( "===" )
print( "def percentage(count, total):" )
print( " return 100 * count / total" )
print( "===" )
sent = ['word1', 'word2', 'word3', 'word4', 'word5', 'word6', 'word7', 'word8', 'word9', 'word10']
print( sent )
print( "===" )
print( "sent[ : 3 ] = ", sent[ : 3 ] )
print( "===" )
print( "sent[ 0 : 3 ] = ", sent[ 0 : 3 ] )
print( "===" )
print( "sent[ 3 : 4 ] = ", sent[ 3 : 4 ] )
print( "===" )
print( "sent[ 4 : ]", sent[ 4 : ] )
print( "===" )
print( "FreqDist( text1 ) = ", FreqDist( text1 ) )
print( "===" )
print( "FreqDist( text1 ).most_common( 50 ) (= 50 most common words in text 1) = ", FreqDist( text1 ).most_common( 50 ) )
print( "===" )
print( "FreqDist( text1 ).hapaxes() (=words occurring only once in text 1) = ", FreqDist( text1 ).hapaxes() )
print( "===" )
print( "FreqDist( text1 )[ 'whale' ] (=how frequently does the word 'whale' occur in text1?) = ", FreqDist( text1 )[ 'whale' ] )
print( "===" )
print( "FreqDist( text1 ).plot( 50, cumulative = True) (=frequency plot of the 50 most occurring words in text1) (close the dialog box to continue) = ", FreqDist( text1 ).plot( 50, cumulative = True) )
print( "===" )
V = set( text1 )
long_words = [ w for w in V if len( w ) > 15]
print( "sorted( long_words ) (=sorted words longer than 15 characters)", sorted( long_words ) )
print( "===" )
fdist5 = FreqDist( text5 )
print ( "sorted( w for w in set( text5 ) if len( w ) > 7 and fdist5[ w ] > 7 ) (= find all words that are longer than 7 characters and have a occur with a frequency of more than 7) = ", sorted( w for w in set( text5 ) if len( w ) > 7 and fdist5[ w ] > 7 ) )
print( "===" )
print( "list( bigrams(['more', 'is', 'said', 'than', 'done'] ) ) = ", list( bigrams(['more', 'is', 'said', 'than', 'done'] ) ) )
print( "===" )
print( "text4.collocations() (=frequent bigrams in text 4) = ", text4.collocations() )
print( "===" )
print( "text8.collocations() frequent bigrams in text 8) = ", text8.collocations() )
print( "===" )
print( "[ len( w ) for w in text1 ] (=get the integer length of all the words in text 1) = ", [ len( w ) for w in text1 ] )
print( "===" )
print( "FreqDist( len( w ) for w in text1 ) = (get the frequency distribution of the integer length of words in text1) = ", FreqDist( len( w ) for w in text1 ) )
fdist = FreqDist( len( w ) for w in text1 )
print ( "fdist.most_common ( 50 ) (=print the 50 most common integer lengths of all the words in text1) = ", fdist.most_common ( 50 ) )
print( "===" )
print ( "fdist.max() (=get the most common integer length of all the words in text1) = ", fdist.max() )
print( "===" )
print ( "fdist[ 3 ] (=get the total occurrence of all words with integer length 3 in text1) = ", fdist[ 3 ] )
print( "===" )
print ( "fdist.freq( 3 ) (=get the proportion of all the words with integer length 3 in text1) = ", fdist.freq( 3 ) )
print( "===" )
fdist1 = FreqDist( text1 ) # create a frequency distribution containing the given samples
fdist1[ text1 ] += 1 # increment the count for this sample
fdist1[ 'monstrous' ] # count of the number of times a given sample occurred
fdist1.freq( 'monstrous' ) # frequency of a given sample
fdist1.N() # total number of samples
fdist1.most_common( 4 ) # the n most common samples and their frequencies
fdist1.tabulate() # tabulate the frequency distribution
fdist1.plot() # graphical plot of the frequency distribution
fdist1.plot( cumulative = True ) #cumulative plot of the frequency distribution
fdist2 = FreqDist( text2 ) # create a frequency distribution containing the given samples
fdist1 |= fdist2 # update fdist1 with counts from fdist2
fdist1 < fdist2	# test if samples in fdist1 occur less frequently than in fdist2
print( "===" )
print( "===" )
print( "===" )


