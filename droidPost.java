package com.proyect.sidec;

import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.util.EntityUtils;

public class httpHandler {
  public String post(String posturl){
	
	try{
		
		HttpClient httpclient = new DefaultHttpClient();
		HttpPost httppost = new HttpPost(posturl);
		
		//Respuesta del servidor
		HttpResponse resp = httpclient.execute(httppost);
		HttpEntity ent = resp.getEntity();
		
		String text = EntityUtils.toString(ent);
		
		return text;
		}catch(Exception e){return "error";}
	}
}
