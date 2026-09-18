#!/usr/bin/env bash
# Elenca i file di una categoria Wikimedia Commons con URL diretto (max 2048px) importabile in Higgsfield.
# Da eseguire nel sandbox Higgsfield:  bash commons_refs.sh "Category:2024 Rolex Paris Masters"
set -e
CAT="$1"; API="https://commons.wikimedia.org/w/api.php"; UA="best-odds-backgrounds/1.0"
curl -sS -A "$UA" -G "$API" --data-urlencode "action=query" --data-urlencode "list=categorymembers" \
  --data-urlencode "cmtitle=$CAT" --data-urlencode "cmlimit=100" --data-urlencode "cmtype=file|subcat" \
  --data-urlencode "format=json" | jq -r '.query.categorymembers[].title' | while IFS= read -r T; do
  case "$T" in Category:*) echo "SUBCAT $T"; continue;; esac
  curl -sS -A "$UA" -G "$API" --data-urlencode "action=query" --data-urlencode "titles=$T" \
    --data-urlencode "prop=imageinfo" --data-urlencode "iiprop=url|size|extmetadata" --data-urlencode "iiurlwidth=2048" \
    --data-urlencode "format=json" | jq -r '.query.pages[] | "\(.title) | \(.imageinfo[0].width)x\(.imageinfo[0].height) | \(.imageinfo[0].extmetadata.LicenseShortName.value // "-") | \(.imageinfo[0].thumburl | sub("\\?.*$";""))"'
done
