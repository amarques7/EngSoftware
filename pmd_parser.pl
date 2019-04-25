#!/usr/bin/perl -w
use strict;
use XML::Simple;
use Data::Dumper;
use Text::CSV;


############################################################
### Entrada: perl check_parser.pl release.xml
### ex: perl check_parser.pl versao.xml
### saida: classes_violacoes.csv classes.csv violacoes.csv
###
### Adriano Marcelo Marques - April 2017
############################################################

############################################################
## declaração de variáveis
############################################################

my $fille = shift;
my $data = 0;
my %count_classes;
my %count_violacoes;
my $xml=new XML::Simple;
my $data=$xml->XMLin($fille);
my @keys = keys $data->{file};
my $temp = 0;
my $nome = $fille;
$nome = substr $nome, 0, rindex( $nome, q{.} );
print "$nome\n";
############################################################
## navegando pela hash
############################################################

foreach my $element(@keys){
		my $vetorHash = $data->{file}{$element}{violation};
	  if ( ref( $vetorHash ) eq 'ARRAY'){
   	
      foreach my $hash ( @{$vetorHash} ){
        (my $temp = $element) =~s/.*\///s;
        $temp =~ s/(.*)\...*/$1/;
     	 	$count_classes{$temp}[0]++;
     	 	$count_classes{$temp}[1]{ $hash->{rule}}++;
        $count_violacoes{$hash->{rule}}++;
        
     	}
    
    }
    #teste esse
    else{
      (my $temp = $element) =~s/.*\///s;
      $temp =~ s/(.*)\...*/$1/;
      $count_classes{$temp}[0]++;
      $count_classes{$temp}[1]{ $vetorHash->{rule}}++;
      $count_violacoes{$vetorHash->{rule}}++;
	}
}
############################################################
## criação de arquivos em csv
############################################################

  open( my $fg, '>', $nome ."_classes.violacoes.csv");
    foreach my $class( sort { $count_classes{$b}[0] <=> $count_classes{$a}[0] }  keys %count_classes ){
      print $fg "$class; \t$count_classes{$class}[0]\n";
      print $fg "lista de violacoes:\n";
      
      foreach my $v ( sort {$count_classes{$class}[1]{$b} <=> $count_classes{$class}[1]{$a}}keys $count_classes{$class}[1] ){
        my $aux1 = $v;
        $aux1 =~ s/[.,^~]//g; 
        print $fg "\t$aux1;$count_classes{$class}[1]{$v}\n";
      }
  }
close $fg;


  open( my $ff, '>', $nome . "_classes.csv" );
    foreach my $class( sort { $count_classes{$b}[0] <=> $count_classes{$a}[0] }  keys %count_classes ){
      print $ff "$class;$count_classes{$class}[0]\n";
    }
  close $ff;


  open( my $fx, '>', $nome . "_violacoes.csv" );
    foreach my $violacao( sort { $count_violacoes{$b} <=> $count_violacoes{$a} }  keys %count_violacoes ){
      my $aux = $violacao;
      $aux =~ s/[.,^ ~ ]//g;
       print $fx "$aux;$count_violacoes{$violacao}\n";
    }
  close $fx;

exit 0; 
