from seqbio.calculation.Seqcal import * 
from seqbio.pattern.SeqPattern import *
from seqbio.seqMan.SeqMan import *

def test_output_function():
    seq = 'ATGGGccGTAGAATTCTTGCaaGCCCGT'
    seq = seq.upper()
    print("Transcription: ", dna2rna(seq))
    print("Transcription-revcomp: ", dna2rna(reverseComplementSeq(seq)))
    print("Translation: ", dna2protein(seq))
    print("Translation-revcomp: ", dna2protein(reverseComplementSeq(seq)))
    print("GC Content:", gcContent(seq))
    print("Count Bases: ", countBasesDict(seq))
    print("Count Bases-revcomp: ", countBasesDict(reverseComplementSeq(seq)))
    print("Search EcoRI: ", enzTargetsScan(seq, 'EcoRI'))
    print("Search EcoRI-revcomp: ", enzTargetsScan(reverseComplementSeq(seq), 'EcoRI'))

def arg_function():
    from argparse import ArgumentParser
    parser = ArgumentParser(prog='myseq', description='Work with sequence')
    subparsers = parser.add_subparsers(
        title='commands', description='Please choose command below:',
        dest='command'
    )
    subparsers.required = True

    cgc_command = subparsers.add_parser('gcContent', help='Calculate GC content')
    cgc_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide sequence")

    count_command = subparsers.add_parser('countBases', help='Count number of each base')
    count_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide sequence")
    count_command.add_argument("-r","--revcomp",action='store_true', default= 'store_false',
                             help="Convet DNA to reverse-complementary")

    transcription_seq_command = subparsers.add_parser('transcription', help='Convert DNA->RNA')
    transcription_seq_command.add_argument("-s", "--seq", type= str, default=None,
                             help="Provide sequence")
    transcription_seq_command.add_argument("-r", "--revcomp", action='store_true', default= 'store_false',
                             help="Convet DNA to reverse-complementary")

    translation_seq_command = subparsers.add_parser('translation', help='Convert DNA->Protein')
    translation_seq_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide sequence")
    translation_seq_command.add_argument("-r", "--revcomp", action='store_true', default= 'store_false',
                             help="Convet DNA to reverse-complementary")

    enzym_seq_command = subparsers.add_parser('enzTargetsScan', help='Find restriction enzyme')
    enzym_seq_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide sequence")
    enzym_seq_command.add_argument("-e", "--enz", type=str, default=None,
                             help="Enzyme name")
    enzym_seq_command.add_argument("-r", "--revcomp", action='store_true', default= 'store_false',
                             help="Convet DNA to reverse-complementary")
    
    return parser

def arg_work():
    parser = arg_function()
    args = parser.parse_args()
    if args.command == 'gcContent':
        if args.seq == None:
            exit(parser.parse_args(['gcContent','-h']))
        seq = args.seq.upper()
        print("Input",args.seq,"\nGC content =", gcContent(seq) )

    elif args.command == 'countBases':
        if args.seq == None:
            exit(parser.parse_args(['countBases','-h']))
        else:
            seq = args.seq.upper()
            if args.revcomp == True:
                 print("Input",args.seq,"\ncountBases =", countBasesDict(reverseComplementSeq(seq))) 
            else:  
                 print("Input",args.seq,"\ncountBases =", countBasesDict(seq)) 
    elif args.command == 'transcription':
        if args.seq == None:
            exit(parser.parse_args(['transcription','-h']))
        else:
            print(args._get_args)
            seq = args.seq.upper()
            if args.revcomp == True:
                 print("Input",args.seq,"\nTanscription =", dna2rna(reverseComplementSeq(seq))) 
            else:  
                 print("Input",args.seq,"\nTranscription =", dna2rna(seq))  
    elif args.command == 'translation':
        if args.seq == None:
            exit(parser.parse_args(['translation','-h']))
        else:
            #print(args._get_args)
            seq = args.seq.upper()
            if args.revcomp == True:
                 print("Input",args.seq,"\nTranslation =", dna2protein(reverseComplementSeq(seq)))   
            else:  
                 print("Input",args.seq,"\nTranslation =", dna2protein(seq)) 
    elif args.command == 'enzTargetsScan':
        if args.seq == None:
            exit(parser.parse_args(['enzTargetsScan','-h']))
        else:
            seq = args.seq.upper()
            #print(args._get_args)
            if args.enz != None:
                if args.revcomp == True:
                    print("Input",args.seq,"\nenzTargetsScan =", enzTargetsScan(reverseComplementSeq(seq), args.enz))
                else:
                    print("Input",args.seq,"\nenzTargetsScan =", enzTargetsScan(seq, args.enz))
            

if __name__ == "__main__":
     arg_work()
     #funct1
     