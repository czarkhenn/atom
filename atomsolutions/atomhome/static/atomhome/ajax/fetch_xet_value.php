<?php
  $contents = file_get_contents('https://coinmarketcap.com/currencies/eternal-token/');
  $doc = new DOMDocument();
  libxml_use_internal_errors(true);
  $doc->loadHTML($contents);
  $xpath = new DOMXpath($doc);
  $articles = $xpath->query('//span[@class="h2 text-semi-bold details-panel-item--price__value"]');
  foreach($articles as $arr) { // DOMElement Object
     echo $arr->textContent;
  }
?>
