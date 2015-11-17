A small script to remove stop words in text files.

nltk stopwords can be combined with stopwords in a given file.

- Usage: 
```sh
 $ for d in path_to_input_dir/*; do
       python stopword_remover.py $d path_to_output_dir/$(basename $d)
   done
```