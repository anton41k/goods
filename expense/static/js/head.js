function list_brand(id,page,brand_goods){
   if (document.getElementById(id).hidden == false)
     document.getElementById(id).hidden = true;
   else
     {document.getElementById(id).hidden = false;
     $.get(("/goods/"+page+"/"+brand_goods),
	function(data){
	$("#"+id).html(data);}); }
}
function all_goods(page){
   if (document.getElementById("all_action").hidden == false)
     document.getElementById("all_action").hidden = true;
   else
     {document.getElementById("all_action").hidden = false;
     $.get(("/goods/"+page+"/all"),
	function(data){
	$("#all_action").html(data);});}
}
function list_spacies(brand) {

   if (document.getElementById(brand).hidden == false)
     document.getElementById(brand).hidden = true;
   else
     {document.getElementById(brand).hidden = false;
     }
}
function subm(clas,page,brand_goods,pk,day,brand) {
	$("."+clas).submit(function(event){event.preventDefault();
	var  form = $('form.'+clas);
	var a=$.ajax({
                type:"POST",
                url:"/goods/"+page+"/"+brand_goods+"/",
		dataType:"json",
		data:form.serialize(),
		success:function(data){
		$('#'+clas).html(data.page);
		  }});
		a.success(function(data){	
		$('#amount'+pk).html(data.amount);});
		a.success(function(data){	
		$('#sum_goods'+pk).html(data.sum_goods);});
		a.success(function(data){	
		$('#sum_day'+brand+day).html(data.sum_day);});
		a.success(function(data){	
		$('#sum'+brand).html(data.sum_all);});
		a.success(function(data){	
		$('#sum_amount'+brand).html(data.sum_amount);});
		a.success(function(data){	
		$('#sum_spacies'+data.spacies).html(data.sum_spacies);});
});}

function subm_allk(clas,pag,pk,day) {
	$("."+clas).submit(function(event){event.preventDefault();
	var  form = $('form.'+clas);
	$.ajax({
                type:"POST",
                url:"/goods/"+pag+"/all/",
		
		data:form.serialize(),
		success:function(data){
			/*$('#all_action').html('');*/
		$('#'+clas).html(data);}});
		
});

}
function subm_all(clas,pag,pk,day) {
	$("."+clas).submit(function(event){event.preventDefault();
	var  form = $('form.'+clas);
	var a=$.ajax({
                type:"POST",
                url:"/goods/"+pag+"/all/",
		dataType:"json",
		data:form.serialize(),
		success:function(data){
			/*$('#all_action').html('');*/
		$('#'+clas).html(data.page);
		/*$('#'+amount).append(json.amount);*/}});
		a.success(function(data){	
		$('#amount_all'+pk).html(data.amount);});
		a.success(function(data){	
		$('#sum_goods_all'+pk).html(data.sum_goods);});
		a.success(function(data){	
		$('#sum_day_all'+day).html(data.sum_day);});
		a.success(function(data){	
		$('#sum_all').html(data.sum_all);});
		a.success(function(data){	
		$('#sum_amount_all').html(data.sum_amount);});
		a.success(function(data){	
		$('.sum_amount_alls').html(data.sum_amount);});
});

}

function month(x,y) {
   if (document.getElementById(x).hidden == false)
     document.getElementById(x).hidden = true;
   else
     document.getElementById(x).hidden = false;
   if (document.getElementById(y).hidden == false)
     document.getElementById(y).hidden = true;
   else
     document.getElementById(y).hidden = false;     
}
function submit_month(page,clas,brand_goods) {
	$(".test_month"+clas).submit(function(event){event.preventDefault();
	var  form = $('form.test_month'+clas);
	$.ajax({
                type:"POST",
                url:"/goods/"+page+"/"+brand_goods+"/",
		data:form.serialize(),
		success:function(data){
			$('#'+clas).html(data);}});});}

function submit_month_all(page) {
	$(".test_month").submit(function(event){event.preventDefault();
	var  form = $('form.test_month');
	$.ajax({
                type:"POST",
                url:"/goods/"+page+"/all/",
		data:form.serialize(),
		success:function(data){
			$("#all_action").html(data);}});});}
