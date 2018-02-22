$(document).ready(function() {


 buttons: ["colvis","excel","print" ];

 $('#button').click(function(){
    var aSum=0;
    var bSum=0;
    var cSum=0;
    var dSum=0;
    var eSum=0;
     $("tbody tr.selected").each(function () {
         var agetValue = $(this).find("td:eq(0)").html();
         var bgetValue = $(this).find("td:eq(1)").html();
         var cgetValue = $(this).find("td:eq(2)").html();
         var dgetValue = $(this).find("td:eq(3)").html();
         var egetValue = $(this).find("td:eq(4)").html();



         aSum +=Number(agetValue)
         bSum +=Number(bgetValue)
         cSum +=Number(cgetValue)
         dSum +=Number(dgetValue)
         eSum +=Number(egetValue)


     });
   $('#avgCPUTimeSelTmp').html(aSum + ' ms');
   $('#avgCPUTimeOnlySelTmp').html(bSum + ' ms');
   $('#avgRealTimeSelTmp').html(cSum + ' ms');
   $('#avgRealTimeOnlySelTmp').html(dSum + ' ms');
   $('#avgMemSelTmp').html(eSum + ' kB');

 });

 //
 var table = $('#timereport').dataTable( {
     "footerCallback": function ( row, data, start, end, display ) {
         var api = this.api(), data;

         // Remove the formatting to get integer data for summation
         var intVal = function ( i ) {
             return typeof i === 'string' ?
                 i.replace(/[,]/g, '')*1 :
                 typeof i === 'number' ?
                     i : 0;
         };

         // Total over all pages
         total = api
             .column( 1 )
             .data()
             .reduce( function (a, b) {
                 return (intVal(a) + intVal(b)).toFixed(1);
             } );

         // Total over this page
         pageTotal = api
             .column( 1, { page: 'current'} )
             .data()
             .reduce( function (a, b) {
                 return (intVal(a) + intVal(b)).toFixed(1);
             }, 0 );


         $( '#avgCPUTimePageTot' ).html(
              pageTotal +' ms'
         );
         $( '#avgCPUTimeTot' ).html(
              total + ' ms'
         );
         // Total over all pages
         total = api
             .column( 2 )
             .data()
             .reduce( function (a, b) {
                 return (intVal(a) + intVal(b)).toFixed(1);
             } );

         // Total over this page
         pageTotal = api
             .column( 2, { page: 'current'} )
             .data()
             .reduce( function (a, b) {
                 return (intVal(a) + intVal(b)).toFixed(1);
             }, 0 );


         $( '#avgCPUTimeOnlyPageTot' ).html(
              pageTotal +' ms'
         );
         $( '#avgCPUTimeOnlyTot' ).html(
              total + ' ms'
         );

         // Total over all pages
         total = api
             .column( 3 )
             .data()
             .reduce( function (a, b) {
                 return (intVal(a) + intVal(b)).toFixed(1);
             } );

         // Total over this page
         pageTotal = api
             .column( 3, { page: 'current'} )
             .data()
             .reduce( function (a, b) {
                 return (intVal(a) + intVal(b)).toFixed(1);
             }, 0 );


         $( '#avgRealTimeTot' ).html(
              pageTotal +' ms'
         );
         $( '#avgRealTimePageTot' ).html(
              total + ' ms'
         );


         // Total over all pages
         total = api
             .column( 4 )
             .data()
             .reduce( function (a, b) {
                 return (intVal(a) + intVal(b)).toFixed(1);
             } );

         // Total over this page
         pageTotal = api
             .column( 4, { page: 'current'} )
             .data()
             .reduce( function (a, b) {
                 return (intVal(a) + intVal(b)).toFixed(1);
             }, 0 );


         $( '#avgRealTimeOnlyTot' ).html(
              pageTotal +' ms'
         );
         $( '#avgRealTimeOnlyPageTot' ).html(
              total + ' ms'
         );


         // Total over all pages
         total = api
             .column( 5 )
             .data()
             .reduce( function (a, b) {
                 return (intVal(a) + intVal(b)).toFixed(1);
             } );

         // Total over this page
         pageTotal = api
             .column( 5, { page: 'current'} )
             .data()
             .reduce( function (a, b) {
                 return (intVal(a) + intVal(b)).toFixed(1);
             }, 0 );


         $( '#avgMemTot' ).html(
              pageTotal +' kB'
         );
         $( '#avgMemPageTot' ).html(
              total + ' kB'
         );



     }
 } );

 $('#timereport tbody').on('click', 'tr', function () {

     $(this).toggleClass('selected');
     $('#button').trigger('click');
     console.log($('#avgCPUTimeSel').html($('#avgCPUTimeSelTmp').html()));
     console.log($('#avgCPUTimeOnlySel').html($('#avgCPUTimeOnlySelTmp').html()));
     console.log($('#avgRealTimeSel').html($('#avgRealTimeSelTmp').html()));
     console.log($('#avgRealTimeOnlySel').html($('#avgRealTimeOnlySelTmp').html()));
     console.log($('#avgMemSel').html($('#avgMemSelTmp').html()));

 } );


 var input = $(".dataTables_filter input");
 input.unbind('keyup search input').bind('keypress', function (e) {
     if (e.which == 13) {
        var keywords = input.val().split(' '), filter ='';
        for (var i=0; i<keywords.length; i++) {
            filter = (filter!=='') ? filter+'|'+keywords[i] : keywords[i];
        }
        table.fnFilter(filter, null, true, false, true, true);
        //                                ^ Treat as regular expression or not
     }
 });

} );
