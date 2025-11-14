import datetime
import time

# Category URL definitions. Originally built to crawl wholesalefashionsquare.com.
# Left in original form for historical context.

womenList = {
    'WOMEN_DRESSES-midiURL': 'https://www.wholesalefashionsquare.com/midi-and-maxi-dresses-s/953.htm',
    'WOMEN_DRESSES-lilBlackDressURL': 'https://www.wholesalefashionsquare.com/little-black-dresses-s/934.htm',
    'WOMEN_DRESSES-miniURL': 'https://www.wholesalefashionsquare.com/mini-dresses-s/952.htm',
    'WOMEN_DRESSES-bodyconURL': 'https://www.wholesalefashionsquare.com/bodycon-dresses-s/610.htm',
    'WOMEN_DRESSES-offTheShoulderURL': 'https://www.wholesalefashionsquare.com/off-the-shoulder-dresses-s/631.htm',
    'WOMEN_DRESSES-formalwearURL': 'https://www.wholesalefashionsquare.com/formal-wear-s/628.htm',
    'WOMEN_TOPS-basicURL': 'https://www.wholesalefashionsquare.com/basics-s/946',
    'WOMEN_TOPS-blousesURL': 'https://www.wholesalefashionsquare.com/blouses-s/948.htm',
    'WOMEN_TOPS-kimonoURL': 'https://www.wholesalefashionsquare.com/kimonos-s/49.htm',
    'WOMEN_TOPS-longMidSleevesURL': 'https://www.wholesalefashionsquare.com/long-sleeve-s/985.htm',
    'WOMEN_TOPS-sleevelessURL': 'https://www.wholesalefashionsquare.com/sleeveless-s/949.htm',
    'WOMEN_TOPS-officewearURL': 'https://www.wholesalefashionsquare.com/office-tops-s/798.htm',
    'WOMEN_SKIRTS-miniURL': 'https://www.wholesalefashionsquare.com/wholesale-mini-skirts-s/961.htm',
    'WOMEN_SKIRTS-midiURL': 'https://www.wholesalefashionsquare.com/wholesale-midi-skirts-s/988.htm',
    'WOMEN_SKIRTS-maxiURL': 'https://www.wholesalefashionsquare.com/wholesale-maxi-skirts-s/962.htm',
    'WOMEN_BOTTOMS-shortsURL': 'https://www.wholesalefashionsquare.com/wholesale-womens-shorts-s/965.htm',
    'WOMEN_BOTTOMS-skinnyURL': 'https://www.wholesalefashionsquare.com/womens-skinny-jeans-s/966.htm',
    'WOMEN_BOTTOMS-wideTrousersURL': 'https://www.wholesalefashionsquare.com/wide-leg-pants-s/967.htm',
    'WOMEN_ROMP-romperURL': 'https://www.wholesalefashionsquare.com/wholesale-rompers-s/959.htm',
    'WOMEN_ROMP-jumpsuitURL': 'https://www.wholesalefashionsquare.com/wholesale-jumpsuits-s/960.htm',
    'WOMEN_ROMP-bodysuitURL': 'https://www.wholesalefashionsquare.com/category-s/746.htm',
    'WOMEN_OUTWEAR-vestURL': 'https://www.wholesalefashionsquare.com/wholesale-vests-s/957.htm',
    'WOMEN_OUTWEAR-jacketURL': 'https://www.wholesalefashionsquare.com/wholesale-jackets-s/7.htm',
    'WOMEN_OUTWEAR-coatURL': 'https://www.wholesalefashionsquare.com/wholesale-coats-s/958.htm',
    'WOMEN_OUTWEAR-sweaterURL': 'https://www.wholesalefashionsquare.com/womens-sweaters-s/950.htm',
    'WOMEN_OUTWEAR-blazerURL': 'https://www.wholesalefashionsquare.com/womens-blazers-s/956.htm',
    'WOMEN_OUTWEAR-bomberJacketURL': 'https://www.wholesalefashionsquare.com/category-s/749.htm',
    'WOMEN_TWOPEICE-twoPieceURL': 'https://www.wholesalefashionsquare.com/2PIECESETS-s/618.htm',
    'WOMEN_LEGGINGS-leggingsURL': 'https://www.wholesalefashionsquare.com/category-s/970.htm',
    'WOMEN_JEANS-jeansURL': 'https://www.wholesalefashionsquare.com/category-s/765.htm',
    'WOMEN_ACTIVEWEAR-activewearURL': 'https://www.wholesalefashionsquare.com/Activewear-s/31.htm',
    'WOMEN_OFFICEWEAR-officewearURL': 'https://www.wholesalefashionsquare.com/womens-business-attire-s/978.htm',
    'WOMEN_CLUBWEAR-clubwearURL': 'https://www.wholesalefashionsquare.com/club-wear-apparel-s/945.htm',
    'WOMEN_INTIMATE-intimatesURL': 'https://www.wholesalefashionsquare.com/womens-intimates-s/29.htm',
    'WOMEN_LACES-lacesURL': 'https://www.wholesalefashionsquare.com/crochet-lace-s/893.htm',
    'WOMEN_TIEDYE-tieDyeURL': 'https://www.wholesalefashionsquare.com/tie-die-s/35.htm'
}

seasonalList = {
    'SEASONAL_FALLWINTER-fallWinterURL': 'https://www.wholesalefashionsquare.com/fall-clothing-s/387.htm',
    'SEASONAL_SPRINGSUMMER-springSummerURL': 'https://www.wholesalefashionsquare.com/summer-clothing-s/731.htm',
    'SEASONAL_SWIMWEAR-swimwearURL': 'https://www.wholesalefashionsquare.com/category-s/801.htm',
    'SEASONAL_BACK2SCHOOL-backToSchoolURL': 'https://www.wholesalefashionsquare.com/category-s/868.htm'
}

plussizeList = {
    'PLUSSIZE_DRESSES-dressesURL': 'https://www.wholesalefashionsquare.com/wholesale-plus-size-dresses-s/11.htm',
    'PLUSSIZE_TOPS-topsURL': 'https://www.wholesalefashionsquare.com/plus-size-tops-s/9.htm',
    'PLUSSIZE_BOTTOMS-bottomsURL': 'https://www.wholesalefashionsquare.com/plus-size-bottoms-s/10.htm',
    'PLUSSIZE_ROMP-rompURL': 'https://www.wholesalefashionsquare.com/plus-size-rompers-s/780.htm',
    'PLUSSIZE_SPRINGSUMMER-springSummerURL': 'https://www.wholesalefashionsquare.com/plus-size-spring-and-summer-s/373.htm',
    'PLUSSIZE_FALLWINTER-fallWinterURL': 'https://www.wholesalefashionsquare.com/plus-size-fall-and-winter-s/327.htm',
    'PLUSSIZE_OUTERWEAR-outerwearURL': 'https://www.wholesalefashionsquare.com/plus-size-outerwear-s/193.htm',
    'PLUSSIZE_FORMALWEAR-formalwearURL': 'https://www.wholesalefashionsquare.com/category-s/769.htm'
}

accessoriesList = {
    'ACCESSORIES_JEWELRY-watchesURL': 'https://www.wholesalefashionsquare.com/watches-s/68.htm',
    'ACCESSORIES_JEWELRY-necklacesURL': 'https://www.wholesalefashionsquare.com/Jewelry-Necklaces-s/59.htm',
    'ACCESSORIES_JEWELRY-earringsURL': 'https://www.wholesalefashionsquare.com/Jewelry-Earrings-s/61.htm',
    'ACCESSORIES_JEWELRY-braceletsURL': 'https://www.wholesalefashionsquare.com/Jewelry-Bracelets-s/62.htm',
    'ACCESSORIES_JEWELRY-ringsURL': 'https://www.wholesalefashionsquare.com/Jewelry-Rings-s/63.htm',
    'ACCESSORIES_SCARFS-scarvesURL': 'https://www.wholesalefashionsquare.com/scarves-s/94.htm',
    'ACCESSORIES_BAGS-bagsURL': 'https://www.wholesalefashionsquare.com/wholesale-bags-s/52.htm',
    'ACCESSORIES_SHOES-shoesURL': 'https://www.wholesalefashionsquare.com/shoes-s/12.htm',
    'ACCESSORIES_HATS-hatsURL': 'https://www.wholesalefashionsquare.com/wholesale-hats-s/738.htm',
    'ACCESSORIES_EYEWEAR-eyewearURL': 'https://www.wholesalefashionsquare.com/wholesale-sunglasses-s/53.htm',
    'ACCESSORIES_MAKEUP-skinCareURL': 'https://www.wholesalefashionsquare.com/category-s/345.htm',
    'ACCESSORIES_MAKEUP-eyesURL': 'https://www.wholesalefashionsquare.com/category-s/348.htm',
    'ACCESSORIES_MAKEUP-lipsURL': 'https://www.wholesalefashionsquare.com/category-s/347.htm',
    'ACCESSORIES_MAKEUP-nailsURL': 'https://www.wholesalefashionsquare.com/category-s/346.htm',
    'ACCESSORIES_MAKEUP-accesoriesURL': 'https://www.wholesalefashionsquare.com/category-s/777.htm',
    'ACCESSORIES_HAIR-hairURL': 'https://www.wholesalefashionsquare.com/hair-accessories-s/56.htm',
    'ACCESSORIES_SOCKS-socksURL': 'https://www.wholesalefashionsquare.com/wholesale-tights-and-socks-s/65.htm'
}

missyList = {
    'MISSY_TOPS-topsURL': 'https://www.wholesalefashionsquare.com/missy-tops-s/791.htm',
    'MISSY_DRESSES-dressesURL': 'https://www.wholesalefashionsquare.com/missy-dresses-s/795.htm',
    'MISSY_ROMP-rompURL': 'https://www.wholesalefashionsquare.com/missy-rompers-s/766.htm'
}

featuredList = {
    'FEATURED-featuredURL': 'https://www.wholesalefashionsquare.com/category-s/1006.htm'
}

promotionsList = {
    'PROMOTIONS_STEALDEAL-stealDealURL': 'https://www.wholesalefashionsquare.com/Wholesale-Off-Price-Apparel-s/47.htm',
    'PROMOTIONS_MISMATCHED-mismatchedURL': 'https://www.wholesalefashionsquare.com/category-s/32.htm'
}

saleList = {
    'SALE-saleURL': 'https://www.wholesalefashionsquare.com/Clothing-Sale-s/27.htm',
    'SALE_FLASHSALE-flashSaleURL': 'https://www.wholesalefashionsquare.com/Flashsale-s/932.htm'
}
