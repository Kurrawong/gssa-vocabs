for i in ../vocabularies/*.ttl; do
  sparql --query ../scripts/make-labels-for-vocab.sparql --results nt --data $i >> ../background-resources/voc-labels.nt
  echo "made labels for $i"
done
